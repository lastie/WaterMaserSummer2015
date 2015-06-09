# This code fits the maser positions and velocity to a Keplerian rotation model and finds the parameter which is the mass of the central black hole. This code only fits the suspected Keplerian portions of the data.

import numpy as np
from scipy.optimize import curve_fit

def func(v, X): #The independent variable has to be the first argument
	return X / (v**2)

data = open("kepPoints.txt", "r")
#data = open("kepPoints2.txt", "r")
#There are four points that matches, let's just use the first one vSys = 596.937

# vSys = 596.937
# x0 = 3.366
# y0 = -1.399
# Mass = 1305415.51381
###########################

# vSys = 597.358
# x0 = 3.316
# y0 = -1.38
# Mass = 1321921.95671
###########################

# vSys = 597.779
# x0 = 3.264
# y0 = -1.351
# Mass = 1338484.9056
###########################

# vSys = 598.201
# x0 = 3.343
# y0 = -1.396
# Mass = 1356299.30927
###########################

#Read each line of the file, store each line into a temp list, access the 3rd and fifth element, calculate r, together with v store into another list

vlist = []
rlist = []
drlist = []

for line in data:
	v = np.absolute(float(line.split(",")[0]) - vSys)
	x = float(line.split(",")[3])
	dx = float(line.split(",")[4]) 
	y = float(line.split(",")[5])
	dy = float(line.split(",")[6])
	r = ((x - x0) ** 2 + (y - y0) **2) ** 0.5
	dr = ((x**2 * dx**2 + y**2 * dy**2) / (x**2 + y**2)) ** 0.5
	if r != 0:
		vlist.append(v)
		rlist.append(r)
		drlist.append(dr)

#import matplotlib.pyplot as plt
#plt.plot(rlist, vlist, r'o')
#plt.show()
#print (rlist, vlist, drlist)

#Conversions
DA = 3.8 * 3.08567758 * 10**22
G = 6.67384 * 10**(-11)
MO = 1.989 * 10**30

rarray = np.array(rlist)
varray = np.array(vlist)
drarray = np.array(drlist)

popt, pcov = curve_fit(f=func, xdata=varray, ydata=rarray, sigma=drarray)
print (popt)
#print (pcov)

#so the parameter is now GM/DA

print (popt[0] * DA / G / MO * (4.848136805555555 * 10**(-9)) * 10**6)

#The answer for the reverse fit is 49273482.0005 Mo

