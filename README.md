audire
======

Audire provides an assistive system for people with hearing disability. Along with speech recognition, the user gets information about different auditory events happening around in the environment which completes the experience of a sound sensing unit.

---

![Screenshot](/screen.png)

### Structure

The project has various modules explained below.

#### Speech Recognition
This functionality is implemented using CMU Sphinx [currently uses Windows Speech Recognition].

#### Direction Detection
This module provides information about the *crude* direction of sound. Right now, the idea is to use analog comparator and find left or right direction.

This module is currently non-functional as it depends on external hardware assistance to gather data about the intensities of sounds from different directions.

#### Anomaly Detection
This module detects anomalous auditory events like knock on doors, car horns etc. The system adapts according to recent sound data and thus doesn't need tuning or extra efforts.

For detecting anomalies, a running average of audio stream is maintained for a fixed window size. The anomalous events are identified if the audio data exceeds the average by an integral multiple of standard deviation of the window.

#### Event Detection
This allows the system to provide information about what (in linguistic terms) is happening around. For example, clapping, drum beats etc. This system can be trained to suite the purpose.

This system works by extracting Mel Frequency Cepstrum Coefficients (MFCC) of incoming audio stream and training a Linear Support Vector Classifier. MFCC features have been previously used successfully for speech recognition tasks, and work well in this case also.

#### User Interface
The user interface communicates with the backend using ajax queries and websocket connection that interacts with a server written using tornado, and displays all necessary information to the user.

### Setup

Dependencies are in `requirements`.

```
pip install -r requirements
```

Run the server and go to [http://localhost:5000/](http://localhost:5000/)

```
cd src
python server.py
```

![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)

© NebulaX TIIC 2015
