#### Selection Sort Algorithm ####

#### Time and Space Complexity ####
"""
Time Complexity: O(N^2)
Auxiliary Complexity: O(1) as the only extra memory used is for temporary variables while swapping two values in Array.
"""


#### Algorithm Explanation ####
"""
Selection Algorithm search for the minimum and place the value at the beginning of the array
start from the first index and assume it's the minimum value then compare with all other indexes if minimum value is
found in other indexes then swap value of first index and minimum value index. now first item is sorted.
then repeat the process for 1, 2, 3...n-1 indexes
"""

arr = list(map(int, input().split()))

for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print(*arr)


# Stabilized Selection Sort Algorithm

"""
To stabilize Selection Sort Algorithm instead of swapping the
elements we put the smaller element in it's correct position.
and move the elements from i to min_index - 1 by one position right.
Thus ensuring smaller element in it's correct position and also
maintaining the greater elements order of positions
"""

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j

    correctValue = arr[min_index]

    while min_index > i:
        arr[min_index] = arr[min_index-1]
        min_index -=1

    arr[i] = correctValue

print(*arr)