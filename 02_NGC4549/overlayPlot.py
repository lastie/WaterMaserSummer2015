# This code is a combination of posvel_6OriginCompare.py and LencMapPlot.py
# This code wants to plot both maps on the same coordinate system
# THis code allows variation of the position of the pos-vel map

data = open("LencMapPoints.txt", "r")
import matplotlib.pyplot as plt
import numpy as np

RA = []
Dec = []

for line in data:
	RA.append(float(line.split()[0]) * 1000)
	Dec.append(float(line.split()[1]) * 1000)

plt.plot(RA, Dec, 'bo', alpha=1)
plt.axis([27000, 28000, -8000, 1000])
#plt.axis([27400, 27600, -6000, -4000])
#plt.axis([27400, 27600, -5500, -4000])
#plt.axis([27450, 27550, -4680, -4610])

##################################

data = open("data2.txt", "r")

ewlist = []
nslist = []

for line in data:
	eastWestOffset = float(line.split(",")[3])
	northSouthOffset = float(line.split(",")[5])
	ewlist.append(eastWestOffset)
	nslist.append(northSouthOffset)

ewlist = np.array(ewlist) + 27529.1
nslist = np.array(nslist) - 4631

plt.plot(ewlist, nslist, color='#D05050', marker='o', alpha=0.5, linestyle='None', markeredgewidth=0)

plt.gca().invert_xaxis()
plt.show()
