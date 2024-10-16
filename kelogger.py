import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print('pressed:', key.char)
    except AttributeError:
        print('pressed:', key)

def on_release(key):
    if key == Key.esc:
        # Stop the listener when the Escape key is pressed
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()