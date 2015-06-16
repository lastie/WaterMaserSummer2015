import numpy as np
import matplotlib.pyplot as plt

vSys = 679.104
data = open("massvSys=" + str(vSys) + ".csv", "r")

vlist = []
mlist = []

for line in data:
	v = float(line.split()[0])
	m = float(line.split()[4])
	vlist.append(v)
	mlist.append(m)

data.close()
x = np.arange(vlist[-1], vlist[0], 0.1)
y = [10**6 for i in range(len(x))]
plt.plot(vlist, mlist, 'bo')
plt.plot(x, y, c='red')
plt.title("vSys=" + str(vSys))
plt.xlabel("Velocity (km/s)")
plt.ylabel("Mass (Mo)")

plt.show()
#plt.savefig("massVelocityvSys=" + str(vSys) + '.png')

