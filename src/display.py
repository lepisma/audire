"""
Module for interacting with display devices
"""

class Display:
    """
    Display device
    """

    def __init__(self, debug = True):
        """
        debug flag sets the display to stdout
        """
        
        self.debug = debug

    def show(self, message):
        """
        Displays the text on device
        """

        if self.debug:
            print(message)
        else:
            print("Output only to stdout is supported currently.")

    def alert(self):
        """
        Alerts user
        """

        if self.debug:
            print("Alert!")
        else:
            print("Output only to stdout is supported currently.")
