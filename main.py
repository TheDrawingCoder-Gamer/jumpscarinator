import wave
import sys
import os
import random
import time

import pyaudio

CHUNK = 1024

possible_files = []

with os.scandir("sounds") as it:
    for entry in it:
        if entry.is_file() and entry.name.endswith('.wav'):
            possible_files.append(entry.name)

# Keep that THANG running!!! hawk tuna!!!
p = pyaudio.PyAudio()

def play_file(file):
    with wave.open(file, 'rb') as wf:
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        while len(data := wf.readframes(CHUNK)):
            stream.write(data)

        stream.close()

# Could be replayed as soon as 2 seconds
LOWER_BOUND = 2
# ... Or as long as 15 minutes
UPPER_BOUND = 15 * 60
# testing: 10s
# UPPER_BOUND = 10

while True:
    file = random.choice(possible_files)
    play_file("sounds/" + file)

    time.sleep(random.uniform(LOWER_BOUND, UPPER_BOUND))



