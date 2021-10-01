# in command prompt, type "pip install pynput" to install pynput.
# If you don't have pip, install it for your OS (The Windows store has a python + pip package)

# To run the program, open a terminal (cmd, powershell, git bash, vscode) and navigate to the directory containing the script
#   Then type:  python W.py
#   You'll know it's working if you start seeing the character 'w' appear after random intervals in a chat box while the program is running

# To stop the program, go to the terminal that it's running in, and press ctrl + c

from pynput.keyboard import Key, Controller
import random
from time import sleep

keyboard = Controller()

# Hits 'w' randomly every 1 to 10 seconds
try:
    while True:
        sleep(random.randint(1,10))
        key = 'w'
        keyboard.press(key)
        keyboard.release(key)   
except KeyboardInterrupt:
    print("Exiting...")
    exit