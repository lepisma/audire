"""
Audio event detection module
"""

import pyaudio
import numpy as np
from array import array
from sys import byteorder

THRESHOLD = 500
CHUNK = 1000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


def is_silent(chunk):
    """
    Returns true if chunk is silent
    """
    
    return np.max(chunk) < THRESHOLD


def trim(data):
    """
    Trim silence from ends
    """

    def _trim(data):
        audio_started = False
        trimmed = array("h")

        for i in data:
            if not audio_started and abs(i) > THRESHOLD:
                audio_started = True
                trimmed.append(i)
            elif audio_started:
                trimmed.append(i)
        return trimmed

    data = _trim(data)
    data.reverse()
    data = _trim(data)
    data.reverse()
    return data


def get_clip(stream):
    """
    Return a clipped audio event
    """

    num_silent = 0
    audio_started = False
    data = array("h")

    while True:
        chunk = array("h", stream.read(CHUNK))
        if byteorder == "big":
            chunk.byteswap()

        data.extend(chunk)

        silent = is_silent(chunk)

        if silent and audio_started:
            num_silent += 1
        elif not silent and audio_started:
            num_silent = 0
        elif not silent and not audio_started:
            audio_started = True
            print("Audio started.")

        if audio_started and num_silent > 10:
            print("Done.")
            break

    return trim(data)
