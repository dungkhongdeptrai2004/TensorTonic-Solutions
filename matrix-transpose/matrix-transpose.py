import numpy as np

def matrix_transpose(A):
   B = []
   N = len(A)
   M = len(A[0])
   for i in range(M):
       add = [0 for j in range(N)]
       B.append(add)
   B = np.array(B)
   for i in range(N):
       for j in range(M):
           B[j][i] = A[i][j]
   return B

   
