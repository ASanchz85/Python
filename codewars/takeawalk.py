#Task:
'''
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
'''

def is_valid_walk(walk):
    
    vertical = 0
    horizontal = 0
    
    for item in walk:
        if item == 'n':
            vertical += 1
        elif item == 's':
            vertical -= 1
        elif item == 'w':
            horizontal += 1
        elif item == 'e':
            horizontal -= 1
        else : return print('wrong input')
    
    if len(walk) == 10 and vertical == 0 and horizontal == 0 : return True
    else : return False
    
    
#Best Answer:
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

#Test Results:
    '''
Walk Validator - fixed tests
should return False if walk is too short
 (2 of 2 Assertions)
should return False if walk is too long
 (3 of 3 Assertions)
should return False if walk does not bring you back to start
 (2 of 2 Assertions)
should return True for a valid walk
 (4 of 4 Assertions)
Completed in 0.18ms
Walk Validator - random tests
Testing a ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] walk
Testing a ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 'n', 'w'] walk
Testing a ['e', 'e', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'e', 's'] walk
Testing a ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 'e', 'w'] walk
Testing a ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'e', 'w'] walk
Testing a ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'e', 'w'] walk
Testing a ['e', 'e', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['e', 'e', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 'e', 'w'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 's', 'w'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 'n', 's', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 's', 'w'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 'n', 's', 'e', 'w'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 'e', 's', 'e', 'w'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 'e', 's', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 'e', 's', 'e', 'w'] walk
Testing a ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 'e', 'n'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 'e', 'n'] walk
Testing a ['s', 'e', 'w', 'w', 'n', 's', 'e', 'w', 'e', 'w'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 'e', 'n'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 'e', 's'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 'e', 's', 'e', 'w'] walk
Testing a ['s', 'e', 'w', 'w', 'n', 's', 'e', 'w', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 'e', 'n'] walk
Testing a ['s', 'w', 'w', 'w', 'n', 's', 'e', 'w', 'e', 'w'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['s', 'w', 'w', 'w', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['s', 'w', 'w', 'w', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 'e', 'n'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 's', 'w'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 's', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 'e', 'n'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 's', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['n', 's', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['n', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['e', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['s', 'w', 'w', 's', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['e', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['e', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['s', 'w', 'w', 'n', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['e', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['s', 'w', 'w', 'n', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['w', 'e', 'e', 'w', 'n', 'w', 's', 's', 'e', 'w'] walk
Testing a ['e', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['s', 'w', 'w', 'n', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['s', 'w', 'w', 'n', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['s', 'w', 'w', 'n', 'n', 's', 'e', 'w', 'e', 'e'] walk
Testing a ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] walk
Testing a ['s', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['s', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['s', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['s', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'n'] walk
Testing a ['e', 's', 'n', 'e', 'w', 'n', 's', 'w'] walk
Testing a ['e', 's', 's', 'n', 'w', 'n', 'n', 's'] walk
Testing a ['e', 'n', 's', 'w', 'w', 'w', 's', 'n', 'e', 'e'] walk
Testing a ['s', 'w', 'w', 'w', 's', 'n', 'e', 'e', 'e', 'n'] walk
Testing a ['w', 'n', 'n', 'w', 's', 'e', 's', 's', 'e', 'n'] walk
Testing a ['s', 'w', 'e', 'e', 'n', 'e', 'w', 'w'] walk
Testing a ['w', 'e', 'n', 'n', 'n', 'e', 'w', 's', 's', 's'] walk
Testing a ['w', 'w', 'e', 's', 'w', 'e', 'e', 'w', 'n', 'e'] walk
Testing a ['w', 'e', 'n', 'e', 'w', 'n', 'w', 's', 'w', 'e'] walk
Testing a ['e', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 'e', 'w'] walk
Testing a ['e', 's', 'n', 'w', 'w', 'e', 'n', 's', 'e', 'e'] walk
Testing a ['s', 'n', 's', 'e', 'n', 's', 's', 'n', 'w', 's'] walk
Testing a ['w', 's', 'e', 'e', 'e', 'n', 'w', 'w'] walk
Testing a ['s', 's', 'w', 's', 'n', 'n', 'e', 'n'] walk
Testing a ['e', 'w', 'n', 's', 'e', 'e', 's', 'n'] walk
Testing a ['w', 'n', 'w', 's', 'w', 'e', 's', 'e', 'n', 'e'] walk
Testing a ['s', 'w', 'w', 'w', 'n', 'e', 'e', 'e'] walk
Testing a ['s', 's', 'n', 'e', 's', 'n', 's', 'w'] walk
Testing a ['w', 'w', 's', 'w', 'e', 'e', 'n', 'e'] walk
Testing a ['w', 'e', 'n', 'n', 'n', 'w', 's', 's'] walk
Testing a ['s', 'e', 'w', 'n', 'e', 'n', 'w', 'e', 's', 'w'] walk
Testing a ['n', 'w', 'w', 'e', 's', 's', 'e', 'e', 'w', 'n'] walk
Testing a ['e', 'e', 'w', 'w', 'n', 'w', 'w', 'e', 'e', 's'] walk
Testing a ['n', 's', 'n', 's', 'w', 'n', 's', 'n'] walk
Testing a ['n', 'n', 'w', 'w', 'e', 's', 's', 'e', 'e', 'w'] walk
Testing a ['e', 'e', 'n', 's', 's', 'w', 'w', 's', 'n', 'n'] walk
Testing a ['s', 'w', 's', 's', 's', 'n', 'e', 'n', 'n', 'n'] walk
Testing a ['s', 's', 'e', 'e', 's', 's', 'n', 'w', 'w', 'n'] walk
Testing a ['n', 's', 'w', 'n', 's', 'n', 'e', 's'] walk
Testing a ['e', 'n', 'n', 'n', 'w', 's', 's', 's'] walk
Testing a ['s', 's', 's', 'n', 's', 's', 'n', 'n', 's', 'n'] walk
Testing a ['n', 's', 'n', 'n', 's', 'n', 's', 's'] walk
Testing a ['s', 'e', 'n', 'n', 'n', 'w', 's', 's'] walk
Testing a ['w', 'n', 's', 's', 'n', 's', 'n', 'n'] walk
Testing a ['e', 'w', 'n', 'e', 'e', 'e', 'e', 's', 'w', 'w'] walk
Testing a ['n', 's', 's', 'w', 'n', 's', 'n', 'n', 'e', 's'] walk
Testing a ['e', 'n', 'w', 'w', 'n', 'w', 's', 'e', 'e', 's'] walk
Testing a ['n', 'n', 'e', 's', 's', 's', 'w', 'n'] walk
Testing a ['w', 'w', 'w', 'w', 'w', 'n', 'e', 'e', 'e', 'e'] walk
Testing a ['s', 's', 'e', 'w', 'w', 'n', 'n', 'w', 'e', 'e'] walk
Testing a ['e', 's', 'e', 'e', 'w', 'n', 'w', 'w'] walk
Testing a ['w', 'w', 'n', 'e', 'n', 'e', 's', 'w'] walk
Testing a ['w', 'n', 'n', 'w', 'n', 's', 's', 'e'] walk
Testing a ['n', 'w', 's', 's', 'w', 'e', 'n', 'n'] walk
Testing a ['n', 's', 'e', 'e', 'w', 'n', 'w', 'w'] walk
Testing a ['n', 'e', 's', 'e', 'w', 'w', 'w', 'n', 'w', 'e'] walk
Testing a ['w', 'e', 'n', 'w', 'n', 'w', 's', 'e'] walk
Testing a ['s', 's', 'w', 'n', 'n', 'n', 'e', 's'] walk
Testing a ['n', 'w', 'e', 'n', 's', 'e', 'w', 's'] walk
Testing a ['n', 'n', 's', 'e', 'w', 's', 'n', 'w'] walk
Testing a ['e', 'w', 'e', 'e', 's', 'e', 'e', 'w', 'w', 'n'] walk
Testing a ['e', 's', 'n', 'n', 'n', 'e', 'n', 's', 's', 's'] walk
Testing a ['n', 'n', 's', 's', 's', 's', 'n', 'n'] walk
Testing a ['w', 'n', 's', 's', 'e', 'e', 's', 'n', 'n', 'w'] walk
Testing a ['n', 'e', 'e', 'w', 's', 'w', 'w', 'e'] walk
Testing a ['s', 'n', 'n', 'e', 'n', 's', 's', 'w'] walk
Testing a ['s', 'w', 'n', 'e', 's', 'e', 's', 'w'] walk
Testing a ['n', 'n', 'w', 'w', 's', 's', 'e', 'e'] walk
Testing a ['e', 'w', 'w', 'e', 'w', 'w', 'e', 'e', 'w', 'e'] walk
Testing a ['w', 'n', 'w', 'w', 'w', 'e', 's', 'e', 'e', 'e'] walk
Testing a ['s', 'n', 'e', 'n', 'n', 'n', 's', 'w', 's', 's'] walk
Testing a ['w', 'w', 's', 'n', 'n', 'e', 'n', 's'] walk
Testing a ['n', 'w', 's', 's', 'w', 'e', 'n', 'n'] walk
Testing a ['e', 'e', 'e', 'e', 'n', 'e', 'w', 'w', 'w', 's'] walk
Testing a ['n', 'w', 'e', 'n', 'n', 's', 'e', 'w', 's', 's'] walk
Testing a ['n', 'n', 'e', 's', 'n', 's', 's', 'w', 'n', 's'] walk
Testing a ['e', 'n', 's', 'n', 'w', 's', 'n', 's'] walk
Testing a ['n', 'n', 's', 'e', 's', 's', 'n', 'w'] walk
Testing a ['w', 'n', 'w', 'n', 'e', 's', 'e', 's'] walk
Testing a ['e', 's', 'e', 'e', 'e', 'w', 'n', 'w', 'w', 'w'] walk
Testing a ['s', 'w', 'w', 'n', 'w', 'n', 'e', 'e', 's', 'e'] walk
Testing a ['w', 's', 's', 'n', 'w', 'n', 'n', 'n', 's', 'e'] walk
Testing a ['n', 'w', 's', 'n', 'e', 'w', 'e', 'n', 's', 'w'] walk
Testing a ['s', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n'] walk
Testing a ['n', 's', 'e', 's', 'n', 's', 'n', 'w', 'n', 's'] walk
Testing a ['w', 's', 'w', 'n', 'e', 'n', 'e', 's'] walk
Testing a ['e', 'w', 'e', 'w', 'w', 'e', 'e', 'w', 'e', 'e'] walk
Testing a ['e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 's', 'e'] walk
Testing a ['w', 'n', 's', 'n', 's', 'e', 's', 'n', 's', 'n'] walk
Testing a ['n', 'n', 'e', 'n', 's', 'w', 's', 'w', 's', 'n'] walk
Testing a ['n', 'n', 's', 'e', 's', 's', 's', 'n', 'w', 'n'] walk
Testing a ['w', 'n', 's', 'n', 'e', 's', 'n', 's'] walk
Testing a ['e', 'e', 's', 'w', 'e', 'w', 'w', 'n', 'e', 'w'] walk
Testing a ['s', 'e', 'e', 'w', 'w', 's', 'w', 'w', 'e', 'e'] walk
Testing a ['w', 'n', 'w', 's', 'n', 's', 'e', 'n'] walk
Testing a ['n', 'n', 'n', 's', 'n', 'w', 's', 's', 'n', 's'] walk
Testing a ['s', 'n', 'n', 'e', 'w', 's', 's', 's', 'w', 'e'] walk
Testing a ['w', 'w', 'w', 's', 'e', 'e', 'e', 'n'] walk
Testing a ['w', 'e', 's', 'n', 'n', 'w', 'n', 's'] walk
Testing a ['w', 'n', 'w', 'e', 'n', 's', 'e', 'w'] walk
Testing a ['e', 'w', 'n', 's', 'w', 'e', 's', 'n'] walk
Testing a ['s', 'w', 's', 'e', 's', 's', 'e', 'n', 'w', 'n'] walk
Testing a ['e', 'e', 'n', 'n', 's', 'e', 'w', 's', 's', 'n'] walk
Testing a ['s', 'e', 's', 'e', 'w', 'n', 'w', 'n', 'w', 'e'] walk
Testing a ['w', 'w', 'w', 's', 'n', 'e', 'e', 'n'] walk
Testing a ['n', 'w', 'w', 'e', 'w', 'e', 'e', 'w'] walk
Testing a ['n', 'n', 'w', 'w', 'n', 's', 's', 'e', 'e', 's'] walk
Testing a ['w', 'e', 'n', 'w', 'w', 'e', 'w', 's', 'e', 'e'] walk
Testing a ['e', 'w', 'e', 's', 'e', 'w', 'e', 'w', 'n', 'w'] walk
Testing a ['e', 'n', 'w', 'e', 'n', 'w', 's', 'e', 'w', 's'] walk
Completed in 8.51ms
You have passed all of the tests! :)
    '''