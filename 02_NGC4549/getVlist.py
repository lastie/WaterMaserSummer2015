data = open("data2.txt", "r")
savefile = open("vlist.txt", "w")

for line in data:
	savefile.write(line.split(",")[0] + "\n")


data.close()
savefile.close()