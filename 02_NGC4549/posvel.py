# Draw a position-velocity map
import matplotlib.pyplot as plt

data = open("redPurple.txt", "r")

vSys = 597.358
x0 = 3.316
y0 = -1.38

rlist = []
vlist = []

for line in data:
	temp = line.split(",")
	v = float(temp[0])
	x = float(temp[3]) - x0
	y = float(temp[5]) - y0
	if v < vSys:
		r = - (x**2 + y**2) ** 0.5
	else:
		r = (x**2 + y**2) ** 0.5
	vlist.append(v)
	rlist.append(r)

plt.plot(rlist, vlist, r'o')
plt.gca().invert_xaxis()
#plt.axis([40, -70, 500, 800])
plt.show()
#plt.savefig("posvel_vSys=597.358.png")
#print (rlist, vlist, drlist)
