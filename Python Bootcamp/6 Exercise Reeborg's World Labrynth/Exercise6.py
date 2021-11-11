def turn_right():
    turn_left()
    turn_left()
    turn_left()
 ##My Code
while front_is_clear():
    move()
    
while not at_goal():
    while wall_on_right() and not wall_in_front():
        move()
    if right_is_clear() and not at_goal():
        turn_right()
        move()
    else: 
        turn_left()
    
##Solution shorter
while front_is_clear():
    move()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move
    else:
        turn_left()