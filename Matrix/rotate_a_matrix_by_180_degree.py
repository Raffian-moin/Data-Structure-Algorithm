"""
Given a square matrix, the task is that turn it by 180 degrees in an anti-clockwise direction without using any extra space.
"""
arr = [[1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12 ], [ 13, 14, 15, 16 ]]

for j in range(len(arr)//2):
    for i in range(len(arr)):
        arr[j][i], arr[len(arr)-j-1][len(arr)-i-1] = arr[len(arr)-j-1][len(arr)-i-1], arr[j][i]

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end = " ")
    print()