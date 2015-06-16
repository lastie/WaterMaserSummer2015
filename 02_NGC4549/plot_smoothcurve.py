#This plot will draw the p-v diagram of NGC 4945 and the fitted curve.
#The fitted value of the X is 1305415.51381
#The input values are:
# vSys = 596.937
# x0 = 3.366
# y0 = -1.399

import matplotlib.pyplot as plt
import numpy as np

data = open('data2.txt', 'r')
rlist = []
vlist = []
drlist = []
vSys = 596.937
x0 = 3.366
y0 = -1.399

for line in data:
	v = float(line.split(",")[0])
	x = float(line.split(",")[3])
	y = float(line.split(",")[5])
	dx = float(line.split(",")[4])
	dy = float(line.split(",")[6])
	dr = ((x**2 * dx**2 + y**2 * dy**2) / (x**2 + y**2)) ** 0.5
	if v > vSys: #if the spot is redshifted, it will appear on the left of origin, but with a positive impact parameter
		r = ((x - x0) ** 2 + (y - y0) **2) ** 0.5
	else:
		r = -((x - x0) ** 2 + (y - y0) **2) ** 0.5
	rlist.append(r)
	vlist.append(np.absolute(v))
	drlist.append(dr)


Y = 304824.82656654
Y2 = 304824.82656654

def upperCurve(x):
	return ( Y / x)**0.5 + vSys

def lowerCurve(x):
	return -( Y2 / (-x))**0.5+ vSys

fig = plt.figure()
rect = fig.patch
rect.set_facecolor('white')

plt.plot(rlist, vlist, color='grey', linestyle = '', marker='o', markersize=4)

i = 0
for error in drlist:
	errorSize = error
	#print (error, "  ", rlist[i])
	plt.plot(rlist[i], vlist[i], color = 'black', linestyle = '', marker = '_', markersize = errorSize, markeredgewidth = 2, alpha = 1)
	#print (errorSize)
	i += 1


#x1 = np.arange(1, 30, 0.1)
#y1 = upperCurve(x1)

#x2 = np.arange(-1, -60, -0.1)
#y2 = lowerCurve(x2)

#plt.plot(x1, y1, 'r-')
#plt.plot(x2, y2, 'b-')

import numpy.ma as ma


x1 = np.arange(5, 40, 0.1)
x2 = np.arange(-90, -10, 0.1)

#rlist_positive = ma.masked_less_equal(rlist, 0)
#rlist_positive = ma.masked_outside(rlist, 5, 40)
#rlist_negative = ma.masked_greater_equal(rlist, 0)
#rlist_negative = ma.masked_outside(rlist, -60, -20)

#print (rlist_positive)
#print (upperCurve(rlist_positive))

#print (rlist_negative)
#print (lowerCurve(rlist_negative))

plt.plot(x1, upperCurve(x1), 'r-')
plt.plot(x2, lowerCurve(x2), 'b-')
plt.axis([-90, 40, 450, 800])

plt.gca().invert_xaxis()
plt.xlabel("Impact parameters with respect to systemic velocity of 596.937km/s (mas)")
plt.ylabel("Velocity (km/s)")
plt.title("Pos-vel diagram with smooth fitting curve for NGC 4945")


#plt.show()
#plt.savefig("posvel_wFit.png")

