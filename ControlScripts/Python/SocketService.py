#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import tornado.websocket

class WSHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    print 'connection opened...'
    self.write_message("Connection was accepted.")

  def on_message(self, message):
    self.write_message("Updating...")
    print 'received:', message
    heating = message[0]
    lighting=message[1]
    oven=message[2]
    print "heating: "+heating+", lighting: "+lighting+" , oven: "+oven
    #updateHeatingStatus(heating)
    #updateLightingStatus(lighting)
    #updateOvenStatus(oven)
    self.write_message("Updated")

  def on_close(self):
    print 'connection closed...'

application = tornado.web.Application([
  (r'/ws', WSHandler),
])

if __name__ == "__main__":
  application.listen(9090)
  tornado.ioloop.IOLoop.instance().start()
