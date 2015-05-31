import matplotlib.pyplot as plt
import numpy as np

Y = 0.04449544604779426
vSys = 4076

def upperCurve(x):
	return ( Y / x)**0.5 + vSys

def lowerCurve(x):
	return -( Y / (-x))**0.5 + vSys

x1 = np.arange(1, 30, 0.1)
y1 = upperCurve(x1)

x2 = np.arange(-1, -60, -0.1)
y2 = lowerCurve(x2)

plt.plot(x1, y1, 'r-')
plt.plot(x2, y2, 'b-')

plt.gca().invert_xaxis()
plt.show()