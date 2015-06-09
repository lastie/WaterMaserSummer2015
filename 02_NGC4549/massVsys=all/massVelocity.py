import numpy as np
import matplotlib.pyplot as plt

vSys = 596.937
data = open("massvSys=" + str(vSys) + ".csv", "r")

vlist = []
mlist = []

for line in data:
	v = float(line.split(";")[0])
	m = float(line.split(";")[4])
	vlist.append(v)
	mlist.append(m)

data.close()
plt.plot(vlist, mlist, 'bo')
plt.plot()
plt.show()

