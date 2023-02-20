import random
import time
import os


def erase_screen():
    try:
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
    except:
        pass


def whos_winner(user, ia_user):
    if ((user == 1 and ia_user == 3) 
        or (user == 2 and ia_user == 1) 
        or (user == 3 and ia_user == 2)):
        return True
    else:
        return False


def statistics(tries, win):
    time.sleep(0.2)
    if tries is 1:
        print(f'You have played {tries} match with a result of {round(win/tries * 100)}% as a win rate\n')
    else:
        print(f'You have played {tries} matches with a result of {round(win/tries * 100)}% as a win rate\n')
    time.sleep(0.8)


def repeat(count: int, victory_count):
    answer = ''
    while True:
        answer = input('Would you like to try again???  (yes = y // no = n)  >>>\n')
        if answer == 'y':
            time.sleep(1)
            erase_screen()
            play(count, victory_count)
        elif answer == 'n':
            quit()
        else:
            continue

def play(count, victory_count):
    if count is 0: 
        print('Welcome to the rock, paper, scissors game >>>')
        victory_count = 0
        time.sleep(2)
    else:
        statistics(count, victory_count)
        
    text = """
            Choose wisely my friend...
            
            [1] > rock
            [2] > paper
            [3] > scissors
            
            """
    print(text)
    count  += 1
    user = ''
    choices = [1, 2, 3]
    
    while not user.isdigit() or int(user) > 3:
        print('Choose a digit between 1 and 3 >>>')
        user = input('')
        
    user = int(user)
    ia_user = random.choice(choices)
    time.sleep(0.5)
    if whos_winner(user, ia_user):
        print('You win !!!\nCongratulations!!!\n')
        victory_count += 1
    else:
        print('You lose this time...\n')
    
    repeat(count, victory_count)
    
erase_screen()
play(0, 0)