import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.colorbar as clb
import numpy as np


# An example for the sake of testing
###################
# rainbow = plt.get_cmap('rainbow')
# cNorm = colors.Normalize(vmin=0, vmax=100)
# scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=rainbow)

#Test & Example
# s = np.ones(10)
# h = np.ones(10)
# v = np.ones(10)
# hsv = np.dstack((h,s,v))
# print (hsv)
# print(type(hsv), hsv[0])
# x = np.arange(0, 10, 0.1)

# for i in range(100):
# 	plt.plot(x[i], x[i], marker = 'o', lw=0, color=scalarMap.to_rgba(i))

# plt.show()

#OMG it worked, I don't really know how but it worked!!
#######################


data = open("data2.txt", "r")
vlist = []
ewlist = []
nslist = []

for line in data:
	eastWestOffset = float(line.split(",")[3])
	northSouthOffset = float(line.split(",")[5])
	v = float(line.split(",")[0])
	ewlist.append(eastWestOffset)
	nslist.append(northSouthOffset)
	vlist.append(v)

rainbow = plt.get_cmap('rainbow')
cNorm = colors.Normalize(vmin=vlist[-1], vmax=vlist[0])

scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=rainbow)

fig = plt.figure(figsize = (8, 6))


for i in range(len(vlist)):
	plt.plot(ewlist[i], nslist[i], marker='o', ms = 8, lw=0, mew=0, color=scalarMap.to_rgba(vlist[i]), alpha=0.5)

# cb1 = clb.ColorbarBase(vlist, cmap=rainbow, norm=cNorm, orientation='horizontal')
# cb1.set_label('Heliocentric Radio Velocity (km/s)')

plt.gca().invert_xaxis()
plt.title("NGC4945 position")
plt.xlabel("East-west offest (mas)")
plt.ylabel("North-south offest (mas)")

#plt.show()
plt.savefig('position_color.png')