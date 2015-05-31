import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b):
	return a*x + b

x = np.linspace(1, 10, 100)
y = 5*x + 2

a, b = curve_fit(f=func, xdata=x, ydata=y)
print(a)