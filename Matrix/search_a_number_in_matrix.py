"""
Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, 
and a number X is given. The task is to find whether element X is present in the matrix or not.
"""
mat = [ [1, 5, 9], [14, 20, 21], [30, 34, 43] ]
number = 14

flag = 0
for i in range (len(mat)):
    for j in range (len(mat[0])):
        if mat[i][j] == number:
            flag = 1
            break

print('YES' if flag == 1 else 'NO')