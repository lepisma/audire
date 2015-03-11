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

level = 0

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


def noise_level():
    global level
    while True:
        snd_data = array("h", stream.read(CHUNK))
        level = np.abs(np.mean(np.array(snd_data)))
        time.sleep(0.1)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
