import numpy as np
def f(x):
	return 2*x**2 + 8*x - 5
def g(x):
  return 4*x + 8

def raphson(x,i,e=0.01,n=20):
  i = i+1
  if(i>n):
    print("Iteration More Than ",n)
    return
  if(np.abs(f(x))<e):
    print(f"Root : {x} , Iteration : {i}")
    return
  x1 = x - f(x)/g(x)
  raphson(x1,i)

raphson(6,0)
# Max Iterate : 50

# Tolerance : 0.01

# First Prediction = 6
