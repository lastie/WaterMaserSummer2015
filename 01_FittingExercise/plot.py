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
Y = 

def upperCurve(x):
	return ( Y / x)**0.5 + vSys

def lowerCurve(x):
	return -( Y / (-x))**0.5 + vSys

plt.plot(rlist, vlist, 'bo')


#x1 = np.arange(1, 30, 0.1)
#y1 = upperCurve(x1)

#x2 = np.arange(-1, -60, -0.1)
#y2 = lowerCurve(x2)

#plt.plot(x1, y1, 'r-')
#plt.plot(x2, y2, 'b-')

#plt.plot(rlist, upperCurve(rlist))

plt.gca().invert_xaxis()
plt.show()

