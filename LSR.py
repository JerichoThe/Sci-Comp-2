import matplotlib.pyplot as plt
import numpy as np
x = [ 1,2,3,4,5,6,7,8]
y = [ 2,5,1,7,9,3,6,10]

x_arr = np.array(x)
y_arr = np.array(y)

A = np.vstack([x,np.ones(len(x_arr))]).T

y_arr = y_arr[ :, np.newaxis]

alpha = np.dot(np.dot(np.linalg.inv(np.dot(A.T, A)),A.T),y_arr)

plt.plot(x_arr,y_arr, 'bo')
plt.plot(x_arr, alpha[0] * x_arr + alpha[1], 'r')
plt.show()