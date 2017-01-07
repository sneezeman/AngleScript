import math
from time import strftime
from Tkinter import Tk
from tkFileDialog import askopenfilename

time = []
angle = []
l = 0

Tk().withdraw() 
track = askopenfilename() 

with open(track, 'rb') as t:
	for line in t.readlines():
		line_massive = line.split(',');
		time.append(line_massive[0])
		try:
			angle.append(round((math.degrees(math.atan2(float(line_massive[3]),float(line_massive[2])))),3));
		except ValueError:
			angle.append('not found')


with open('results.txt', 'w') as r:
	r.write(strftime("%Y-%m-%d %H:%M:%S") + '\n')
	for l in range(len(time)):
		r.write(str(time[l])+ '\t' +  str(angle[l]) + '\n')
