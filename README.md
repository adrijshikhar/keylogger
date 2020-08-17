# keylogger

A python3 script to capture and log every key stroke on linux based systems. This script uses [`pyxhook.py`](https://github.com/JeffHoogland/pyxhook) under the hood.

## Usage

### Requirements

[`python3.8`](https://www.python.org/downloads/release/python-380/) is required to run this application.

Clone the repository and run the following command to install the dependenices.

```bash
pip3 install -r requirements.txt
```

You may need `python-xlib` externally. To install it follow the commands for your system

#### Arch based systems

```bash
sudo pacman -S python-xlib
```

#### Ubuntu based systems

```bash
sudo apt install python-xlib
```

### Run

Once everything is setup, copy `.env.example` file to `.env` in the same folder and make the required changes. Define the file location where you want to keep the logs and define a grave key which will kill the keylogger.

After creating `.env` file, run the following command in terminal to enable keylogger.

```bash
python3 keylogger.py
```

### Extras

You can add  `python3 keylogger.py` to your startup scripts to automatically start logging on start up.
