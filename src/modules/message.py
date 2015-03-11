"""
Speech module
Fallback mode : windows speech recognition
"""

import speech


def speech_win(websocket_handler):
    """
    Write speech data to websocket handler
    Works on windows speech system
    """
    while True:
        phrase = speech.input()
        websocket_handler.write_message("message:" + phrase)

        
def speech_cmu(websocket_handler):
    """
    Write speech data to websocket handler
    Works on CMU Sphinx
    """
    pass
