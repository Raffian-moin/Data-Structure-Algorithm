"""
Given a 2D square matrix, print the Principal and Secondary diagonals.
"""
mat = [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ] ]
first=[]
second=[]

for i in range(len(mat)):
    first.append(mat[i][i])
    second.append(mat[i][len(mat[0])-i-1])

print(*first)
print(*second)