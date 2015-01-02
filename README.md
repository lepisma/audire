tmp
===

This branch has code for interfacing with CMU Sphinx.

*Will be merged eventually with master.*

###Structure

- `/res` contains static resources like language model and dictionaries for Sphinx.
- `/src` contains the source
- `/tests` contains unit tests

###Plan

The idea is to have a program that monitors microphone for *hotwords* and fires actions based on the interpretation of the sentence, most of the time which will be a speech-to-text display. This will mostly need a nice integration of simple python scripts with pocketSphinx with a bit of language model tuning.

Next in queue is firing analysis threads on the audio signals to perform event detection on non-speech audio. This part will need experimentation on various methods and finally implementing in (fast) native code using C++ or using the inbuilt DSP of beagle.

![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)

© NebulaX TIIC 2015
