"""
Anomaly Detection using moving window
"""

import pyaudio
import numpy as np
from array import array
from sys import byteorder

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

AVG_TIME = 10.0
AVG_CHUNKS = RATE * AVG_TIME / CHUNK


def anomaly_detection(websocket_handler):
    """Write the result of anomaly detection to given socket object
    """
    window = np.zeros(AVG_CHUNKS)
    window_mean = 0.0
    window_var = 0.0

    previous_state = 0
    
    while True:
        chunk = array("h", stream.read(CHUNK))
        if byteorder == "big":
            chunk.byteswap()
        data = np.array(chunk)
        chunk_mean = np.mean(np.abs(data))

        if (chunk_mean - window_mean) > (3 * np.sqrt(window_var)):
            if previous_state == 0:
                websocket_handler.write_message("anomaly:1")
                previous_state = 1
        else:
            if previous_state == 1:
                websocket_handler.write_message("anomaly:0")
                previous_state = 0
    
        window_var += ((window[-1] - chunk_mean) *
                       (((chunk_mean - window[-1]) / AVG_CHUNKS) +
                        (2 * window_mean)) +
                       (chunk_mean**2 - window[-1]**2)) / AVG_CHUNKS
    
        window_mean += (chunk_mean - window[-1]) / AVG_CHUNKS
        window = np.roll(window, 1)
        window[0] = chunk_mean
