# Formula = M = v^2*D*theta/G

v = 150* 10**3 # in meters per second
D = 3.7 * 3.08567758 * 10**22 # in meters
theta = (0.121**2+1.622**2)**0.5 * 4.84813681 * 10**(-9) # in radian
G = 6.67384 * 10**(-11) # in m^3/kg/s^2
MO = 1.989 * 10**30

n = 1.4 * 10**6

#print (str(v**2 * D * theta / G / MO))
print (str((G*n*MO/D/theta)**0.5/1000))


# The anser is 1.4 * 10**6 and this is correct in SI units