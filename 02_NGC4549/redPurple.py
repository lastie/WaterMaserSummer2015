#This code will take input vSys = 563km/s, and a grid of suspected black hole coordinates, and fit for black hole mass separately with the red and purple blobs and compare those values. 

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x0_list = np.arange(-10, -1.5, 0.5) 
y0_list = np.arange(-10, -2.5, 0.5)
# x0_list = [-10.   -9.5  -9.   -8.5  -8.   -7.5  -7.   -6.5  -6.   -5.5  -5.   -4.5 -4.   -3.5  -3.   -2.5  -2. ]
#y0_list = [-10.   -9.5  -9.   -8.5  -8.   -7.5  -7.   -6.5  -6.   -5.5  -5.   -4.5  -4.   -3.5  -3. ]


vSys = 563 #km/s

savefile = open("redPurpleResultTable_2.txt", "w")


#A function that uses scientific notation, with the second input as how mani decimal points you would want, the returned value is a string with the appearance of scientific notation
def scien(num, deci): 
	mag = int(np.floor(np.log10(num)))
	sigfig = np.around([num / (10**mag)], deci)
	return (str(sigfig[0]) + "e" + str(mag))

for x0 in x0_list:
	for y0 in y0_list:
		data = open("redPurple.txt", "r")
		vlist_R = [] #red
		rlist_R = []
		drlist_R = []

		vlist_P = [] #purple
		rlist_P = []
		drlist_P = []

		for line in data:
			templist = list(map(float, line.split(",")))
			v = np.absolute(templist[0] - vSys)
			x = templist[3]
			dx = templist[4]
			y = templist[5]
			dy = templist[6]
			r = ((x - x0) ** 2 + (y - y0) **2) ** 0.5
			dr = ((x**2 * dx**2 + y**2 * dy**2) / (x**2 + y**2)) ** 0.5

			if templist[0] > 700:
				vlist_R.append(v)
				rlist_R.append(r)
				drlist_R.append(dr)
			else:
				vlist_P.append(v)
				rlist_P.append(r)
				drlist_P.append(dr)

		data.close()

		def func(v, X):
			return X / (v**2)

		DA = 3.8 * 3.08567758 * 10**22
		G = 6.67384 * 10**(-11)
		MO = 1.989 * 10**30

		popt_R, pcov_R = curve_fit(f=func, xdata=vlist_R, ydata=rlist_R, sigma=drlist_R)
		popt_P, pcov_P = curve_fit(f=func, xdata=vlist_P, ydata=rlist_P, sigma=drlist_P)

		mass_R = popt_R[0]* DA / G / MO * (4.848136805555555 * 10**(-9)) * 10**6
		mass_P = popt_P[0]* DA / G / MO * (4.848136805555555 * 10**(-9)) * 10**6

		savefile.write(str(x0) + ' ' + str(y0) + ' ' + scien(mass_R, 4) + ' ' + scien(mass_P, 4) + ' ' + scien(mass_R - mass_P, 4) + '\n')


savefile.close()



