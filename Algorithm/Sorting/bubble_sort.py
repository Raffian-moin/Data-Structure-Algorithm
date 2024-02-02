#### Bubble Sort Algorithm ####

#### Time and Space Complexity ####
"""
Time Complexity: O(N^2)
Auxiliary Complexity: O(1) as the only extra memory used is for temporary variables while swapping two values in Array.
"""

#### Algorithm Explanation ####
"""
Bubble Algorithm swap the adjacent elements if previous index value is greater than next index value.
Thus is puts the max value at the end of the array after first iteration
start from the first index and compare with second index. if first > second, then swap and continue the process for the rest of the indexes
thus after first iteration last element is the greatest
after second iteration last two indexes are the greatest
and continue the process
"""


arr = [1, 2, 9, 6, 4, 3, 5, 8, 7, 10]

for i in range(len(arr)):
    # Last ith elements are already sorted
    # so exclude them for comparison in current iteration
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)