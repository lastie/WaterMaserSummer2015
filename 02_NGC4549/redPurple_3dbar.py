from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

data = open("redPurpleResultTable.txt", "r")

x0_list = []
y0_list = []
diff_list = []

for line in data:
	templine = list(map(float,line.split()))
	x0_list.append(templine[0])
	y0_list.append(templine[1])
	diff_list.append(templine[2] - templine[3])

data.close()

ax.bar3d(x0_list, y0_list, [0]*len(x0_list), dx=0.25, dy=0.25, dz=diff_list, alpha=0.8)
ax.set_xlabel("eastWest offest")
ax.set_ylabel("northsouth offset")
ax.set_zlabel("Difference in fitted mass")

plt.savefig("redPurple3dBar.png")


