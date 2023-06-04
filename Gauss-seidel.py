import numpy as np
x = [
    [10,4,5],
    [1,6,1],
    [3,1,6]
]

y = [8,5,10]

def gauss_seidel(x_list, y_list, e = 0.01, n = 15):
  x_arr = np.array(x)
  y_arr = np.array(y)

  #check
  diagonals = np.array(np.diag(x_arr))
  np.fill_diagonal(x_arr,0)
  not_diagonals = np.array(np.sum(np.abs(x_arr),1))

  if(np.all(diagonals < not_diagonals)):
    print("Not Diagonally Dominant")
    return False
  
  arr_old = np.zeros(np.shape(x_list[0]))
  x_arr = -x_arr

  for i in range(n):
    arr_new = np.array(arr_old)
    print("iter",i)
    print("array", arr_new)

    for j, row in enumerate(x_arr):
      arr_new[j] = (y_arr[j]+np.dot(row, arr_new))/diagonals[j]

      # check
      gap = arr_new - arr_old
      euclid = np.sqrt(np.dot(gap,gap))

    if(euclid < e):
      print("Solved")
      return True

    arr_old = arr_new

gauss_seidel(x,y)
