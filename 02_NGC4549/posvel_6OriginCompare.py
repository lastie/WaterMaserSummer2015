# Draw a position-velocity map for NGC 4945 with the choice of specifying the BH position
import matplotlib.pyplot as plt

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

# x0 = -12.3095 #Choose the BH center to be at vSys
# y0 = -10.5324

def plot(x0, y0, plot_index, vSys):
	_rlist = []
	for i in range(len(vlist)):
		x = xlist[i] - x0
		y = ylist[i] - y0
		if vlist[i] < vSys: #So that the blue shifted and rs have negative and positive values on the axis
			r = - (x**2 + y**2) ** 0.5
		else:
			r = (x**2 + y**2) ** 0.5
		_rlist.append(r)

	#print (_rlist, vlist)

	plt.subplot(2, 3, plot_index)
	plt.plot(_rlist, vlist, 'bo')
	plt.gca().invert_xaxis()
	plt.title("vSys = " + str(vSys))

#plt.axis([40, -70, 500, 800])


# plot(-12.6705, -10.9484, 1, 564.069)
# plot(-12.2645, -10.6394, 2, 563.648)
# plot(-12.3095, -10.5324, 3, 563.227)
# plot(-11.7535, -10.1864, 4, 562.805)
# plot(-12.7965, -10.7354, 5, 561.12)
# plot(-12.1825, -10.4614, 6, 560.699)

#All these bigger numbers don't change the shape of the central blob... Try lowering the numbers.
# plot(-11.7625, -10.1954, 1, 560.278)
# plot(-11.4835, -10.2454, 2, 559.856)
# plot(-11.6705, -10.5274, 3, 559.435)
# plot(-11.9435, -10.7454, 4, 559.014)
# plot(-11.9335, -10.7144, 5, 558.592)
# plot(-11.7365, -10.5794, 6, 558.171)

# plot(-11.5495, -10.5184, 1, 557.75)
# plot(-11.5375, -10.5424, 2, 557.329)
# plot(-11.5985, -10.5824, 3, 556.907)
# plot(-11.6165, -10.5834, 4, 556.486)
# plot(-11.5825, -10.5264, 5, 556.065)
# plot(-11.5105, -10.5264, 6, 555.643)

#I need a small section to get the vSys, x, y, and the index). I think I'll just specify the starting velocity

vPlot, xPlot, yPlot = [], [], []
count = 6
switch = 0

for i in range(len(vlist)):
	if vlist[i] == 598.201:
		switch = 1
	if switch == 1 and count > 0:
		vPlot.append(vlist[i])
		xPlot.append(xlist[i])
		yPlot.append(ylist[i])
		count -= 1
	elif count == 0:
		break

# print (vPlot)
# print (xPlot)
# print (yPlot)

for i in range(len(vPlot)):
	print (i, vPlot[i], xPlot[i], yPlot[i])
	plot(xPlot[i], yPlot[i], i+1, vPlot[i])

# plot(-15.427999999999997, -15.036899999999999, 1, 544.97299999999996) 
# plt.xlabel("Guess: dx = -15.4, dy = -15.03, vSys = 544.98")
plt.show()
#plt.savefig("posvel_guess.png")
#print (rlist, vlist, drlist)

