import numpy as np
x = [
    [
        [4, 2, 1],
        [2, 6, -3],
        [-1, 2, 7]
    ],
    [
        [80, 6, 12],
        [5, 160, -7],
	    [1, 10, 180]
    ],
    [
        [6,1,2],
        [-2,4,1],
        [1,2,8]
    ]
]
y = [
    [8,3,1],
    [1500,1200,1000],
    [12,5,10]
]
import numpy as np

def gauss_seidel(x_list, y_list, e = 0.001, n=20):
  x_arr = np.array(x_list)
  y_arr = np.array(y_list)

  diagonals = np.array(np.diag(np.abs(x_arr)))
  not_diagonals = np.array(np.sum(np.abs(x_arr),1)-diagonals)

  if(np.all(diagonals < not_diagonals)):
    print("Not diagonally dominant")
    return False

  diag = np.array(np.diag(x_arr))
  np.fill_diagonal(x_arr,0)
  
  
  

  arr_old = np.zeros(np.shape(x_list[0]))
  x_arr = -x_arr

  for i in range(n):
    arr_new = np.array(arr_old)
    for j, row in enumerate(x_arr):
      arr_new[j] = (y_arr[j]+np.dot(row, arr_new))/diag[j]
    print("Iter", i+1)
    print("Array",arr_new)

    gap = arr_new - arr_old
    euclid = np.sqrt(np.dot(gap,gap))

    if(euclid < e):
      print("Solved")
      return True

    arr_old = arr_new


for x,y in zip(Xs,Ys):
  print(f"X : {x}, Y : {y}")
  gauss_seidel(x,y)
