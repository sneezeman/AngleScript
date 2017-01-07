import math
import numpy as np
from time import strftime
x = []
y = []
t = []
newGrid = [0, 1]
newData = []
angle = []
i = 0
l = 0
k = 1
f = open('track_1.txt');
for line in f.readlines():
	line_massive = line.split(',');
	t.append(float(line_massive[0]))
	x.append(line_massive[2]);
	y.append(line_massive[3]);
	
	try:
	    angle.append(math.degrees(math.atan2(float(line_massive[3]),float(line_massive[2]))));
	except ValueError:
	    angle.append(angle[i-1])
	i = i+1

newGrid[0] = ((float(t[0])*1000 - math.fmod(float(t[0])*1000, 50))/1000)
newGrid[1] = (newGrid[0]+ 0.05)

while newGrid[k] < (t[i-1]):
	newGrid.append(newGrid[k-1]+ 0.05)
	k = k+1

k = 0
while newGrid[k] < (t[i-1]):
	newData.append(np.interp (newGrid[k],t,angle))
	k = k+1

	
f.close()
f = open('results.txt', 'w');
f.write(strftime("%Y-%m-%d %H:%M:%S") + '\n')
for l in range(i):
    f.write(str(t[l])+ '\t' +  str(angle[l]) + '\n')
    l = l+1;

f.close()

l = 0;

f = open('results_interp.txt', 'w');
f.write(strftime("%Y-%m-%d %H:%M:%S") + '\n')

for l in range(k-1):
	if (l % 2) == 1:
		f.write(str(round(newGrid[l],2))+ '\t' +  str(round(newData[l],2)) + '\n')
    #l = l+1;

f.close()