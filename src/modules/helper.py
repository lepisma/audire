"""
Helper functions for training event classifier
"""

from events import *
import pyaudio

def record_events():
    """Record events and return a list of data with class number.
    """

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    names = []
    data = []
    target = []
    target_id = 0
    while True:
        name = (raw_input("Enter the event name or `q` for exiting: "))
        if name == "q":
            break
        else:
            names.append(name)
        iter = int(raw_input("Enter the number of samples for this class: "))
        for _ in range(iter):
            print("Taking sample #" + str(_ + 1))
            audio = get_clip(stream)
            data.append(audio)
            target.append(target_id)
        print("")
        target_id += 1
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    return [data, target, names]
