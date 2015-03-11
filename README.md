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

#### Anomaly Detection
This module detects anomalous auditory events like knock on doors, car horns etc. The system adapts according to recent sound data and thus doesn't need tuning or extra efforts.

#### Event Detection
This allows the system to provide information about what (in linguistic terms) is happening around. For example, clapping, drum beats etc. This system can be trained to suite the purpose.

![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)

© NebulaX TIIC 2015
