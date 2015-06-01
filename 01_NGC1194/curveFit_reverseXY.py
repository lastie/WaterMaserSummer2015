# This code fits the maser positions and velocity to a Keplerian rotation model and finds the parameter which is the mass of the central black hole.

import numpy as np
from scipy.optimize import curve_fit

def func(v, X): #The independent variable has to be the first argument
	return X / (v**2)

data = open("data_red.txt", "r")
x0 = 513.942
y0 = 509.307

#Read each line of the file, store each line into a temp list, access the 3rd and fifth element, calculate r, together with v store into another list

vlist = []
rlist = []
drlist = []

for line in data:
	v = np.absolute(float(line.split()[1]) - 4076)
	x = float(line.split()[3])
	dx = float(line.split()[4]) 
	y = float(line.split()[5])
	dy = float(line.split()[6])
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
DA = 52.4 * 3.08567758 * 10**22
G = 6.67384 * 10**(-11)
MO = 1.989 * 10**30

rarray = np.array(rlist)
varray = np.array(vlist)
drarray = np.array(drlist)

popt, pcov = curve_fit(f=func, xdata=varray, ydata=rarray, sigma=drarray)
print (popt)
#print (pcov)

#so the parameter is now GM/DA

print (popt[0] * DA / G / MO * (4.848136805555555 * 10**(-10)) * 10**6)

#The answer for the reverse fit is 49273482.0005 Mo

