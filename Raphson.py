import numpy as np

def f(x):
  return x**2 - 5

def g(x):
  return 2*x

def raphson(x0, e):
  x1 = x0 - f(x0)/g(x0)

  if(np.abs(f(x1)) < e):
    print("Root = ", x1)
    return

  raphson(x1,e)

raphson(2, 0.1)
raphson(12, 0.1)
