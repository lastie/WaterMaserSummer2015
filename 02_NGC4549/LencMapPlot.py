data = open("LencMapPoints.txt", "r")
import matplotlib.pyplot as plt
import numpy as np

RA = []
Dec = []

for line in data:
	RA.append(float(line.split()[0]) * 1000)
	Dec.append(float(line.split()[1]) * 1000)

plt.plot(RA, Dec, "bo")
plt.axis([27000, 28000, -8000, 1000])

plt.gca().invert_xaxis()
plt.xlabel("Right Ascension J2000 (mas)")
plt.ylabel("Declination J2000 (mas")
plt.title("NGC 4945 - 2005 epoch Australian LBA map")


#plt.show()
plt.savefig("ALBAmap.png")