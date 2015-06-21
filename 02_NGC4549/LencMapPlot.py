# Reproduces the plot from Lenc paper in units of 'mas'
# Half of the program is commented out; because I need the second half of the program to draw the original map(in original degrees and time units) and overlay the positions of Lenc and Greenhill.

data = open("LencMapPoints.txt", "r")
import matplotlib.pyplot as plt
import numpy as np

RA = []
Dec = []

# for line in data:
# 	RA.append(float(line.split()[0]) * 1000*15)
# 	Dec.append(float(line.split()[1]) * 1000)

for line in data:
	RA.append(float(line.split()[0]))
	Dec.append(float(line.split()[1]))

plt.plot(RA, Dec, "bo")
#plt.axis([27000*15, 28000*15, -8000, 1000])
plt.axis([27, 28, -8, 1])
plt.plot(27.48, -5.4, "ro")

plt.gca().invert_xaxis()
# plt.xlabel("Right Ascension J2000 (mas)")
# plt.ylabel("Declination J2000 (mas")
# plt.title("NGC 4945 - 2005 epoch Australian LBA map")

plt.xlabel("Right Ascension J2000 (only has seconds)")
plt.ylabel("Declination J2000 (only has arcseconds)")
plt.title("NGC4945: Overlay of positions of Greenhill and Lenc")


#plt.show()
#plt.savefig("ALBAmap.png")
plt.savefig("ALBAmap_overlay.png")
