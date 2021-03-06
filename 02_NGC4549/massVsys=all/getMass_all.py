#This code will calculate the Blackhole mass for each data poing, with an input of the origin: systemic velocity, x0 and y0.
import numpy as np
data = open("data2.txt", "r")

vlist, xlist, ylist = [], [], []

for line in data:
	temp = line.split(",")
	v = float(temp[0])
	x = float(temp[3])
	y = float(temp[5])
	vlist.append(v)
	xlist.append(x)
	ylist.append(y)

# This equation is from the Greenhill paper, the unit for v is km/s and the unit for r is mas.
def getMass(v, r):
	return 1.1* v**2 * 3.77 * r

# I generated data files for the following systemic velocites:
# x0 = -12.3095
# y0 = -10.5324
# vSys = 563.227

# x0 = -0.097
# y0 = -0.614
# vSys = 700.172

# x0 = -2.256
# y0 = -2.927
# vSys = 663.934

# x0 = -11.2385
# y0 = -9.9794
# vSys = 546.657

for index in range(len(vlist)):

	x0 = xlist[index]
	y0 = ylist[index]
	vSys = vlist[index]


	savefile = open("massVsys=" + str(vSys) + ".csv", "w")

	for i in range(len(vlist)):
			x = xlist[i] - x0
			y = ylist[i] - y0
			v = vlist[i] - vSys
			r = (x**2 + y**2) ** 0.5
			mass = getMass(v, r)
			if mass != 0:
				digi = int(np.log10(mass))
				flag = (digi >= 6)
			else:
				digi = '0'
				flag = 'CENTER'
				#print(v, x, y, mass)
			savefile.write(str(v+vSys) + ' ' + str(v) + ' ' + str(x) + ' ' + str(y) + ' ' + str(mass) + ' ' + str(digi) + ' ' + str(flag))
			savefile.write('\n')
			
	savefile.close()
