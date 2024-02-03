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


arr = list(map(int, input().split()))

for i in range(len(arr)):
    # Last ith elements are already sorted
    # so exclude them for comparison in current iteration
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)

# Bubble Sort Algorithm in O(n) time complexity when array is already sorted

"""
In bubble sort we swap elements only when current element is
greater than next element. Keeping this in mind in an iteration,
if no swap is performed means that all the next elements are in
ascending order so we don't need to perform swaps for those elements.
And we can stop sorting.
"""

for i in range(len(arr)):
    # Last ith elements are already sorted
    # so exclude them for comparison in current iteration
    swap = False
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap = True

    if swap == False:
        break

print(*arr)