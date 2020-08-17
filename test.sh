#!/bin/bash

set +x

python3 keylogger.py -&
pid=$!
sleep 2000 &
xdotool key Caps_Lock &> /dev/null
xdotool key ~ &> /dev/null
kill $pid
wait $pid

# Local .env
if [ -f .env ]; then
    # Load Environment Variables
    export $(cat .env | grep -v '#' | awk '/=/ {print $1}')
    if grep -q ascii $LOG_LOCATION; then
        echo found
    else
        echo found but file does not end with grave key
        exit 125
    fi
fi
