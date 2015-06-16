import numpy as np

#A function that uses scientific notation, with the second input as how mani decimal points you would want, the returned value is a string with the appearance of scientific notation
def scien(num, deci): 
	mag = int(np.floor(np.log10(num)))
	sigfig = np.around([num / (10**mag)], deci)
	return (str(sigfig[0]) + "e" + str(mag))

print(scien(100000, 3))
print(scien(1234567, 2))

