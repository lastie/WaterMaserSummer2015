#This plot will draw the p-v diagram of NGC 1194 and the fitted curve.
#The fitted value of the X is 9.17784456e+12

import matplotlib.pyplot as plt
import numpy as np

data = open('data.txt', 'r')
rlist = []
vlist = []
x0 = 514.182
y0 = 509.230
vSys = 4076

for line in data:
	v = float(line.split()[1])
	x = float(line.split()[3])
	y = float(line.split()[5])
	if v > vSys: #if the spot is redshifted, it will appear on the left of origin, but with a positive impact parameter
		r = ((x - x0) ** 2 + (y - y0) **2) ** 0.5
	else:
		r = -((x - x0) ** 2 + (y - y0) **2) ** 0.5
	rlist.append(r)
	vlist.append(np.absolute(v))

#Y = 9.17784456 * 10**12 * (4.84813681 * 10**(-9)) * 10**(-6) # modulated constant based on current the units of v(km/s) and theta (mas), converted from m/s and rad, respectively
#Y = 0.04449544604779426
Y = 9.17784456 * 10**12 #This number was only obtained based on the redshifted part of the data... so It makes sense that only that part matches
# The unit of this plot should be in pixels.
Y2 = 1.33749466* 10**13 # This is the fitted number for the blue dots

def upperCurve(x):
	return ( Y / x)**0.5 / 1000 + vSys

def lowerCurve(x):
	return -( Y2 / (-x))**0.5 / 1000 + vSys

plt.plot(rlist, vlist, 'bo')


#x1 = np.arange(1, 30, 0.1)
#y1 = upperCurve(x1)

#x2 = np.arange(-1, -60, -0.1)
#y2 = lowerCurve(x2)

#plt.plot(x1, y1, 'r-')
#plt.plot(x2, y2, 'b-')

import numpy.ma as ma



#rlist_positive = ma.masked_less_equal(rlist, 0)
rlist_positive = ma.masked_outside(rlist, 5, 40)
#rlist_negative = ma.masked_greater_equal(rlist, 0)
rlist_negative = ma.masked_outside(rlist, -60, -20)

print (rlist_positive)
print (upperCurve(rlist_positive))

print (rlist_negative)
print (lowerCurve(rlist_negative))

plt.plot(rlist_positive, upperCurve(rlist_positive), 'r-')
plt.plot(rlist_negative, lowerCurve(rlist_negative), 'g-')
plt.axis([-60, 40, 3000, 5000])

plt.gca().invert_xaxis()
#plt.show()
plt.savefig("posvel_wFit.png")

