# Problem Source: https://www.enjoyalgorithms.com/blog/move-all-the-zeroes-to-the-end

# Problem Statement
# Given an array X[] of n integers, where some elements are zero and 
# some elements are non-zero. Write a program to move all the zeroes 
# to the end of the array.

arr = list(map(int, input().split()))

currentIndexOfZero = 0

for i in range(len(arr)):
    
    if arr[i] != 0:
        if currentIndexOfZero != i:
            arr[currentIndexOfZero] = arr[i]
            arr[i] = 0
        currentIndexOfZero +=1

print(arr)