import numpy as np

# NUMPY ARRAYS COPY BY REFERENCE!!!

# manually create array
a = np.array([[1,4],[3,4],[2,5],[7,6]])

# randomly create (big) array
twoDarray = np.zeros([34,50], int)
threeDarray = np.zeros([34,50,23], int)

# modify a patch
# CAREFUL!
a[i:,j:,k] != a[i:][j:][k]
# CAREFUL!
a[i:,j:,k:] != a[i:][j:][k:]
# a[i:,j:,k:] is all scalars a[x][y][z] st x>=i, y>=j, z>=k
# a[i:][j:][k:] means take i-th and above subarrays, from this object take all j-th and above subarrays, from this object take all k-th and above subarrays.
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23]], dtype=uint8)
>>> b[1:,2:]
array([[ 6,  7],
       [10, 11],
       [14, 15],
       [18, 19],
       [22, 23]], dtype=uint8)
>>> b[1:][2:]
array([[12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23]], dtype=uint8)


# matrix multiplication: use dot
>>> np.dot(array([(a,b),(c,d),(e,f)]),array([g,h]))
array([a*g + b*h,  c*g + d*h,  e*g + f*h])
