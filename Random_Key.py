# in command prompt, type "pip install pynput" to install pynput.
# If you don't have pip, install it for your OS (The Windows store has a python + pip package)

# To run the program, open a terminal (cmd, powershell, git bash, vscode) and navigate to the directory containing the script
#   Then type:  python Random_Key.py
#   this script will log actions to the console that it's running in, you can verify operational status there.

# To stop the program, go to the terminal that it's running in, and press ctrl + c
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as mController

import random
from time import sleep

keyboard = Controller()
mouse = mController()

# Choose a random action every 10 seconds, either mouse or keyboard
# then either click or enter the keystroke
try:
    while True:
        sleep(random.randint(1,10))
        action = random.randint(0,1)
        keys = ['w', 'a', 's', 'd']

        print("action is: ", action)

        # click the mouse
        if action == 0:
            mouse.click(Button.left)

        # hit a key
        if action == 1:
            index = random.randint(0,3)
            key = (keys[index])
            print("key is: ", key)
            keyboard.press(key)
            keyboard.release(key)
except KeyboardInterrupt:
    print("Exiting...")
    exit