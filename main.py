import wave
import sys
import os
import random
import time

import pyaudio

CHUNK = 1024
SAMPLE_RATE=48000


possible_files = []

with os.scandir("sounds") as it:
    for entry in it:
        if entry.is_file() and entry.name.endswith('.wav'):
            possible_files.append(entry.name)

# Keep that THANG running!!! hawk tuna!!!
p = pyaudio.PyAudio()


# I COULD get away with opening this only on each play, but then it's not controllable via the system wide volume control
# Opening it here requires that all input files be of the format specified here
stream = p.open(format=pyaudio.paInt16, channels=2, rate=SAMPLE_RATE, output=True)

def play_file(file):
    with wave.open(file, 'rb') as wf:
        while len(data := wf.readframes(CHUNK)):
            stream.write(data)


# Could be replayed as soon as 2 seconds
LOWER_BOUND = 2
# ... Or as long as 15 minutes
UPPER_BOUND = 15 * 60
# testing: 10s
#UPPER_BOUND = 10

try:
    while True:
        file = random.choice(possible_files)
        play_file("sounds/" + file)

        time.sleep(random.uniform(LOWER_BOUND, UPPER_BOUND))
except KeyboardInterrupt:
    stream.close()
    p.terminate()
    print("Exiting")


