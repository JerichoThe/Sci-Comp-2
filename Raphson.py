import numpy as np
def f(x):
	return 2*x**2 + 8*x - 5

def g(x):
	return 4*x + 8

def raphson(x0,e=0.01,t=50):

	if(np.abs(f(x0)) < e):
		print("Root = ", x0)
		return

	x1 = x0 - f(x0)/g(x0)
	raphson(x1)
    
raphson(6)
# Max Iterate : 50

# Tolerance : 0.01

# First Prediction = 6
