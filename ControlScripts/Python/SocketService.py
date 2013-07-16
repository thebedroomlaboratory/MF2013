#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import tornado.websocket
#import tornado.template

#Method to ensure only 1 or 0 can be passed otherwise -1 is passed to indicate an error
def validate(val):
  if int(val) == 1:
		return val
	elif int(val) ==0:
		return val
	else:
		return "-1"  

class WSHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    print 'connection opened...'
    self.write_message("Connection was accepted.")

  def on_message(self, message):
    self.write_message("Updating...")
    print 'received:', message
    heating = validate(message[0])
    lighting = validate(message[1])
    oven = validate(message[2])
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
