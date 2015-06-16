# This code is an updated version of the massVelocity.py, which draws asingle mass vs. velocity diagram. This code will draw all the mass vs. velocity diagrams, except for some data points with repeated V, in which case the V point read in first would be overwritten.

import numpy as np
import matplotlib.pyplot as plt

data = open("data2.txt", "r")

vlist = []

for line in data:
	v = float(line.split(",")[0])
	vlist.append(v)

data.close()

for i in range(len(vlist)):
	data2 = open("massVsys=" + str(vlist[i]) + ".csv", "r")
	_vlist = []
	_mlist = []
	for line in data2:
		if line:
			#print (line)
			v = float(line.split()[0])
			m = float(line.split()[4])
			_vlist.append(v)
			_mlist.append(m)
			#print (i, vlist[i], v,m)

	data2.close()

	x = np.arange(_vlist[-1], _vlist[0], 0.1)
	y = [10**6 for i in range(len(x))]

	plt.plot(_vlist, _mlist, 'bo')
	plt.plot(x, y, c='red')
	plt.title("vSys=" + str(vlist[i]))
	plt.xlabel("Velocity (km/s)")
	plt.ylabel("Mass (Mo)")

	plt.savefig("massVelVsys=" + str(vlist[i]) + '.png')
	plt.clf()

	print(i)
