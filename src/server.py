"""
Tornado websocket server
"""

import tornado.ioloop
import tornado.web
import tornado.websocket
import os
from threading import Thread
from modules import noise, anomaly, message, event

settings = {"static_path": os.path.join(os.path.dirname(__file__), "static")}

# Runt the audio level thread
Thread(target=noise.noise_level).start()


class IndexHandler(tornado.web.RequestHandler):
    """Handle rendering of dash
    """
    def get(self):
        self.render("index.html")


class EventHandler(tornado.web.RequestHandler):
    """Event detection route handler
    """
    def get(self):
        # Event detection results
        self.write(event.get_event())


class LevelHandler(tornado.web.RequestHandler):
    """Audio Level request handler
    """
    def get(self):
        # Make a global level var
        # Update it using a threaded script
        # Return its value here
        self.write(str(noise.level))


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    """
    Handle messages from server to dash.
    Work involves sending anomaly values and speech to text values.
    """
    def open(self):
        print("WebSocket Opened")
        # Pass the object to different modules
        # so that they can communicate with the dash

        Thread(target=anomaly.anomaly_detection, args=(self, )).start()
        Thread(target=message.speech_win, args=(self, )).start()
    
    def on_message(self, message):
        print("Received a message : " + message)

    def on_close(self):
        print("WebSocket closed")

    
application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/event", EventHandler),
    (r"/level", LevelHandler),
    (r"/ws", WebSocketHandler)
], **settings)

if __name__ == "__main__":
    application.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
