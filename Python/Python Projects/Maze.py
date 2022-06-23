#go to link:http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def deadend():
    turn_right()
    turn_left()

#commands
#at_goal()
#front_is_clear()
#right_is_clear()
#wall_in_front()
#wall_on_right()
#is_facing_north()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        while wall_in_front():
            if wall_in_front() and wall_on_right():
                turn_left()
            elif wall_in_front and right_is_clear():
                turn_right()
            elif front_is_clear() and right_is_clear():
                turn_right()
            elif front_is_clear() or right_is_clear():
                turn_right()
            elif front_is_clear() and not right_is_clear():
                move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
