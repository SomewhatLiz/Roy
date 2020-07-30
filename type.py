from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def type(key, times):
    for char in key:
        if not isinstance(char, str):
            return True
    for time in range(times):
        for char in key:
            if isinstance(char, str):
                keyboard.press(char)
                keyboard.release(char)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def checkType(comment, lastComment):
    if comment.body != lastComment:
        if isinstance(comment.body, str):
            type(comment.body, 1)
