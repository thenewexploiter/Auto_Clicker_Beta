# cmd command1: pip | (is show your wersion of pip)
# cmd command2: pip install pynput | (pack to auto clicker)


__author__ = 'thenewexploiter'

print("███████████████████████████████████████████████████████████████████")
print("██▀▄─██▄─██─▄█─▄─▄─█─▄▄─███─▄▄▄─█▄─▄███▄─▄█─▄▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█")
print("██─▀─███─██─████─███─██─███─███▀██─██▀██─██─███▀██─▄▀███─▄█▀██─▄─▄█")
print("▀▄▄▀▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀")
print(" ")
print("The Start Stop Key: R")
print("Exit Key: M")
print("Made By: " + __author__)
print(" ")
print("Output:")

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.001
button = Button.left
start_stop_key = KeyCode(char='r')
exit_key = KeyCode(char='m')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True
        print("Auto Clicker: On")

    def stop_clicking(self):
        self.running = False
        print("Auto Clicker: Off")

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()
