"""
A matrix is a two-dimensional array that consists of rows and columns. 
It is an arrangement of elements in horizontal or vertical lines of entries.
"""
arr = [[1, 2, 3], [4, 5, 6]]

for i in range (len(arr)):
    for j in range (len(arr[0])):
        print(arr[i][j], end=' ')
    print()