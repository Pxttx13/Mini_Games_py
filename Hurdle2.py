import random
def turnright():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    move()
    turn_left()
    move()
    turnright()
    move()
    turnright()
    move()
    turn_left()
    
while not at_goal():
    jump()