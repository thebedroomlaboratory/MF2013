#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import tornado.websocket
import json
#import tornado.template

def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input 

class WSHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    print 'connection opened...'
    self.write_message("Connection was accepted.")

  def on_message(self, message):
    self.write_message("Updating...")
    print 'received:', message 
    result = convert(json.loads(message))
    for key, value in result.items():
      print key, value
    #heating = validate(message[0])
    #lighting = validate(message[1])
    #oven = validate(message[2])
    #print "heating: "+heating+", lighting: "+lighting+" , oven: "+oven
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
