"""
Tornado websocket server
"""

import tornado.ioloop
import tornado.web
import tornado.websocket
import os

settings = {"static_path": os.path.join(os.path.dirname(__file__), "static")}


class IndexHandler(tornado.web.RequestHandler):
    """Handles rendering of dash
    """
    def get(self):
        self.render("index.html")


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    """Handles messages from server to dash"""
    def open(self):
        print("WebSocket Opened")
    
    def on_message(self, message):
        print("Client received a message : " + message)
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

    
application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/ws", WebSocketHandler)
], **settings)

if __name__ == "__main__":
    application.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
