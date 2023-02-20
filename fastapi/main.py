from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    age: int
    id: int

users_list = [User(id=1, name="Pepe", surname="euiros", age=19),
              User(id=2, name="Luousn", surname="Speor", age=51),
              User(id=3, name="Kiesn", surname="Pankl", age=29)]

@app.get("/")
async def root():
    return users_list 

@app.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
    

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}