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
    
for rep in range(6):
    jump()