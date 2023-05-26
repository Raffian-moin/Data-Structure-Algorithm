from collections import defaultdict

"""
Given a matrix mat[][] having n rows and m columns. We need to find unique elements in the matrix i.e, those elements not repeated in the matrix or those whose frequency is 1.
"""
mat = [[1, 2, 3, 20], [5, 6, 20, 25], [1, 3, 5, 6], [6, 7, 8, 15]]
d=defaultdict(int)
for i in range(len(mat)):
    for j in range(len(mat[0])):
        d[mat[i][j]]+=1

for keys in d:
    if d[keys]==1:
        print(keys, end = " ")