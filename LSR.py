x = [0,1,2,3,4,5,6,7,8,9]
y = [4,2,9,4,2,6,9,3,7,10]
import matplotlib.pyplot as plt
import numpy as np

x_arr = np.array(x)
y_arr = np.array(y)

A = np.vstack((x,np.ones(len(x_arr)))).T

y_arr = y_arr[ :, np.newaxis]

alpha = np.dot(np.linalg.pinv(A),y_arr)
print(alpha)

plt.plot(x_arr,y_arr,'bo')
plt.plot(x_arr,alpha[0] * x_arr + alpha[1], 'r')
plt.show()
