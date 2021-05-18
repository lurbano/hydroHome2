#! /usr/bin/python3

# From: https://www.hackster.io/dataplicity/control-raspberry-pi-gpios-with-websockets-af3d0c

import os.path
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import tornado.gen
import RPi.GPIO as GPIO
import time
import subprocess
import json
import sys
import argparse
import asyncio
#from numpy import arange, mean
import numpy as np
#from oledU import *
import os
import glob



#Tornado Folder Paths
settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "static")
	)

#pyPath = '/home/pi/rpi-led-strip/pyLED/'

#Tonado server port
PORT = 8040

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		print ("[HTTP](MainHandler) User Connected.")
		self.render("index.html")


class WSHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		print ('[WS] Connection was opened.')
		self.write_message('{"who": "server", "info": "on"}')
		#self.oled = oledU(128,32)


	async def on_message(self, message):
		print ('[WS] Incoming on_message:', message)
		try:
			msg = json.loads(message)
			if msg["what"] == "server":
				if msg["opts"] == "off":
					sys.exit("Stopping server")

			# LED STRIP (2/3)


			if msg["what"] == "Temperature":
				print("checking temperature ")

				os.system('modprobe w1-gpio')
				os.system('modprobe w1-therm')

				base_dir = '/sys/bus/w1/devices/'
				device_folder = glob.glob(base_dir + '28*')[0]
				device_file = device_folder + '/w1_slave'

				def read_temp_raw():
					f = open(device_file, 'r')
					lines = f.readlines()
					f.close()
					return lines

				def read_temp():
					lines = read_temp_raw()
					while lines[0].strip()[-3:] != 'YES':
						time.sleep(0.2)
						lines = read_temp_raw()
					equals_pos = lines[1].find('t=')
					if equals_pos != -1:
						temp_string = lines[1][equals_pos+2:]
						temp_c = float(temp_string) / 1000.0
						temp_f = temp_c * 9.0 / 5.0 + 32.0
						return temp_f

					print(read_temp())

				t = read_temp()
				print(t)


				#return message
				self.write_message({"info":"temperature", "value":str(t)+"°F"})

			if msg["what"] == "turnon":
				print("turning on")
				subprocess.Popen('sudo python3 /home/pi/hydroHome2/webServer/pumpOn.py', shell=True)
				self.write_message({"info":"turnon", "value":"pumping now"})

				if msg["what"] == "turnoff":
					print("turning off")
					subprocess.Popen('sudo python3 /home/pi/hydroHome2/webServer/pumpOff.py', shell=True)
					self.write_message({"info":"turnoff", "value":"pumping stopped"})





			if msg["what"] == "restart":

				subprocess.Popen('sleep 5 ; sudo python3 '+os.path.join(os.path.dirname(__file__), "server.py" + f' -n {nPix}'), shell=True)
				main_loop.stop()

			if msg["what"] == "reboot":

				subprocess.Popen('sleep 5 ; sudo reboot', shell=True)
				main_loop.stop()



		except Exception as e:
			print(e)
			print("Exception: Error with data recieved by server")
			print(message)


	def on_close(self):
		print ('[WS] Connection was closed.')



application = tornado.web.Application([
  (r'/', MainHandler),
  (r'/ws', WSHandler),
  ], **settings)


if __name__ == "__main__":
	try:
		http_server = tornado.httpserver.HTTPServer(application)
		http_server.listen(PORT)
		print("hello")
		main_loop = tornado.ioloop.IOLoop.instance()

		print ("Tornado Server started")



		# LED STRIP (END)

		# get ip address
		cmd = "hostname -I | cut -d\' \' -f1"
		IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
		print('IP: '+ IP +":" + str(PORT))
		#oled.write('IP: '+ IP, 3)
		cmd = 'iwgetid | sed \'s/.*://\' | sed \'s/"//g\''
		wifi = subprocess.check_output(cmd, shell=True).decode("utf-8")
		#oled.write(wifi, 2)
		print(wifi)

		main_loop.start()




	except:
		print ("Exception triggered - Tornado Server stopped.")


#End of Program
