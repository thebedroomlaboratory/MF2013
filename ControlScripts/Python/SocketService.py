#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import threading
import time
import sharedVariables

def start_tornado(*args, **kwargs):
	application = tornado.web.Application([
		(r'/ws', WSHandler),
	])
	application.listen(9090)
	#print("Starting Tornado")
	tornado.ioloop.IOLoop.instance().start()
	#print "Tornado finished"

def convert(input):
	if isinstance(input, dict):
		return {convert(key): convert(value) for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [convert(element) for element in input]
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input

def stop_tornado():
		ioloop = tornado.ioloop.IOLoop.instance()
		ioloop.add_callback(lambda x: x.stop(), ioloop)
		#print "Asked Tornado to exit"

class WSHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		#print 'connection opened...'
		self.write_message("Connection was accepted.")

	def on_message(self, message):
		self.write_message("Updating...")
		print 'Overrides:', message 
		result = convert(json.loads(message))
		for key, value in result.items():
			#print key, value
			if (key == "heat_onoffswitch"):
				sharedVariables.heatOverride = value
			elif (key == "light_onoffswitch"):
				sharedVariables.lightOverride = value
			elif (key == "oven_onoffswitch"):
				sharedVariables.bagelOverride = value
		#heating = validate(message[0])
		#lighting = validate(message[1])
		#oven = validate(message[2])
		#print "heating: "+heating+", lighting: "+lighting+" , oven: "+oven
		#updateHeatingStatus(heating)
		#updateLightingStatus(lighting)
		#updateOvenStatus(oven)
		self.write_message("Updated")

# Example Usage:
if __name__ == "__main__":
	t = threading.Thread(target=start_tornado)	
	t.start()
	while True:
		try:
			time.sleep(5)
			#print("Still running")
		except KeyboardInterrupt:
			stop_tornado()
			t.join()
			exit()
