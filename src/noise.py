"""
Module to get the noise level in the environment
"""

import pyaudio
import numpy as np
from array import array
import time

CHUNK = 1000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

while True:
    snd_data = array("h", stream.read(CHUNK))
    print np.mean(np.array(snd_data))
    time.sleep(0.1)

stream.stop_stream()
stream.close()
p.terminate()
