from gpiozero import Robot 
import curses 
robot = Robot(left=(18,23), right = (12,20)) 



actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
    }

def main(window):
    next_key = None
    while True:
	curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY DOWN
            curses.halfdelay(1)
            action = actions.get(key)
            if action is not None:
		
                if key == 261 or key == 260:
                    action(0.85)
                    print(key)
                else:
                	action(0.45)
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY UP
            robot.stop()

curses.wrapper(main)
