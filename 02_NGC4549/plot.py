import matplotlib.pyplot as plt

data = open("data2.txt", "r")

ewlist = []
nslist = []

for line in data:
	eastWestOffset = float(line.split(",")[3])
	northSouthOffset = float(line.split(",")[5])
	ewlist.append(eastWestOffset)
	nslist.append(northSouthOffset)

plt.plot(ewlist, nslist, 'o')
plt.gca().invert_xaxis()
plt.show()
#plt.savefig("position.png")