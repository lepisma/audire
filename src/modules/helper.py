"""
Helper functions for training event classifier
"""

import event
from classify import train, preprocess
import cPickle


def record_events():
    """Record events and return a list of data with class number.
    """

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
            audio = event.get_clip(event.stream)
            data.append(preprocess(audio, event.RATE))
            target.append(target_id)
        print("")
        target_id += 1
    
    event.stream.stop_stream()
    event.stream.close()
    event.p.terminate()

    print("Training classifier")
    classifier = train(data, target)
    print("Training done, dumping data")
    cPickle.dump(names, open("events.pkl", "w"))
    cPickle.dump(classifier, open("model.pkl", "w"))
    cPickle.dump([data, target], open("data.pkl", "w"))
    print("All done.")

    
if __name__ == "__main__":
    record_events()
