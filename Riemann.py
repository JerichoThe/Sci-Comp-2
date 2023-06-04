import numpy as np

def f(x):
  return x**2 -5

a = 2
b = 5
n = (b-a)+2

lebar_kotak = (b-a)/(n-1)
x = -np.linspace(a,b,n)
y = f(x)

leftReiman = lebar_kotak * sum(y[:n-1])
rightReiman = lebar_kotak * sum(y[1:])

x_mid = (x[:n-1] + x[1:]) / 2
y_mid = f(x_mid)

midPoint = lebar_kotak * sum(y_mid)

trapezoid = lebar_kotak / 2 * (y[0] + 2 * sum(y[1:n-1]))

print(leftReiman)
print(rightReiman)
print(midPoint)
print(trapezoid)
