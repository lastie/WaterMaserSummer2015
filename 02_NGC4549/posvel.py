# Draw a position-velocity map
import matplotlib.pyplot as plt

data = open("data2.txt", "r")

vSys = 651
rlist = []
vlist = []

for line in data:
	temp = line.split(",")
	v = float(temp[0])
	x = float(temp[3])
	y = float(temp[5])
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
#print (rlist, vlist, drlist)
