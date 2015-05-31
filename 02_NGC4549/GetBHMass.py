# This code fits the maser positions and velocity to a Keplerian rotation model and finds the parameter which is the mass of the central black hole.

import numpy as np
from scipy.optimize import curve_fit

def func(r, X): #The independent variable has to be the first argument
	return (X/r)**0.5

data = open("data2.txt", "r")

#Here enter the systemic velocity and the reference position points
x0 = 0
y0 = 0
vSys = 560

#Read each line of the file, store each line into a temp list, access the 3rd and fifth element, calculate r, together with v store into another list

vlist = []
rlist = []
drlist = []
Mlist = []

for line in data:
	temp = line.split(",")
	v = np.absolute(float(temp[0]) - vSys)
	x = float(temp[3])
	dx = float(temp[4]) 
	y = float(temp[5])
	dy = float(temp[6])
	r = ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5
	dr = ((x**2 * dx**2 + y**2 * dy**2) / (x**2 + y**2)) ** 0.5
	M = 1.1 * (v**2) * (3.77) * (r)
	print (v, r, M)
	if r > 0:
		vlist.append(v)
		rlist.append(r)
		drlist.append(dr)


#Conversions
DA = 3.7 * 3.08567758 * 10**22
G = 6.67384 * 10**(-11)
MO = 1.989 * 10**30

rarray = np.array(rlist)
varray = np.array(vlist) * 10**3
drarray = np.array(drlist)

popt, pcov = curve_fit(f=func, xdata=rarray, ydata=varray, sigma=drarray)
print (popt)
#print (pcov)

#so the parameter is now GM/DA

print (popt[0] * DA / G / MO * (4.848136805555555 * 10**(-9)))
print (len(rarray))

