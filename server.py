# -*- coding:utf-8 -*-

import socket
import threading
import logging
import sys
import MySQLdb

HOST = "192.168.137.27"
PORT = 1220
MAX_CLI = 10

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

try:
	db = MySQLdb.connect(host="localhost", user="###", passwd="###", db="hoop")
except:
	logging.info("MySQL connection error")

cursor = db.cursor()

try:
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((HOST, PORT))
	server_socket.listen(MAX_CLI)
except socket.error, e:
	logging.info("Socket error: %s" %e)
	sys.exit(1)

global onlines
global sockets
onlines = {}
sockets = {}

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

class newSocket(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True:
			self.conn, self.addr = server_socket.accept()
			logging.info("Got connection from %s:%s" %(self.addr[0], self.addr[1]))
			connection = Connection(self.conn, self.addr)
			connection.start()

class Connection(threading.Thread):
	def __init__(self, conn, addr):
		threading.Thread.__init__(self)
		self.conn = conn
		self.addr = addr

	def run(self):
		while True:
			self.login()

	def login(self):	
		self.credentials = self.conn.recv(1024)
		if self.credentials:
			if self.credentials[0] == "$":
				self.username = strip_non_ascii(self.credentials.split(" ")[0][1:])
				self.password = self.credentials.split(" ")[1]
				self.password = self.password.strip()
				
				cursor.execute("SELECT password FROM accounts WHERE username=%s", [self.username])
				data = cursor.fetchall()
				
				if len(data) == 0:
					self.conn.send("RST")
				if data[0][0] == strip_non_ascii(self.password):
					cursor.execute("SELECT username2 FROM friends WHERE username1=%s", [self.username])
					friends = cursor.fetchall()
					friend_list = ""

					if len(friends) == 0:
						friend_list = "$"

					for i in range(0,len(friends)):
						friend_list = friend_list + friends[i][0] +"$" 

					self.conn.send("ACK" + "$$" + friend_list)
					onlines[self.username] = self.conn

					while True:
						self.buf = self.conn.recv(1024)
						if self.buf:
							if self.buf[0] == "!": # If message contains add friend request
								self.friend_uname = self.buf.split(' ')[0][1:]
								cursor.execute("INSERT INTO friends (username1, username2) VALUES (%s, %s)", (self.username, self.friend_uname))
								db.commit()
							else:
								self.to_user = strip_non_ascii(self.buf.split("-")[0])
								self.msg = strip_non_ascii(self.buf.split("-")[1])
								onlines[self.to_user].send(self.username + "-" + self.msg)
					
				else:
					self.conn.send("RST")

			if self.credentials[0] == "#": # If has got a new membership request
				self.reg_username = strip_non_ascii(self.credentials.split(" ")[0][1:])
				self.reg_password = strip_non_ascii(self.credentials.split(" ")[1])
				self.reg_password = self.reg_password.strip()
				
				try:
					cursor.execute("INSERT INTO accounts (username, password) VALUES(%s,%s)", (self.reg_username,self.reg_password))
					db.commit()
					self.conn.send("2003")
				except:
					self.conn.send("3003")

	def send_msg(self, msg):
		to_user = msg.split(',')[0]
		msg = msg.split('-', 1)[1]
		onlines[to_user].send(msg)

logging.info("Server started!")
logging.info("Listening on %s:%s" %(HOST, PORT))

new_socket= newSocket()
new_socket.start()

while True:
	msg = raw_input()
	connection.send_msg(msg)
