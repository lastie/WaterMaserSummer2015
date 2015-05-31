# Draw a position-velocity map for NGC 4945 with the choice of specifying the BH position
import matplotlib.pyplot as plt

data = open("data2.txt", "r")

vSys = 560
rlist = []
vlist = []
x0 = -11.4835 #Choose the BH center to be at 550
y0 = -10.2454

for line in data:
	temp = line.split(",")
	v = float(temp[0])
	x = float(temp[3]) - x0
	y = float(temp[5]) - y0
	if v < vSys: #So that the blue shifted and rs have negative and positive values on the axis
		r = - (x**2 + y**2) ** 0.5
	else:
		r = (x**2 + y**2) ** 0.5
	vlist.append(v)
	rlist.append(r)

plt.plot(rlist, vlist, r'o')
plt.gca().invert_xaxis()
#plt.axis([40, -70, 500, 800])
#plt.show()
plt.savefig("posvel_vSys=560.png")
#print (rlist, vlist, drlist)
