#### Bubble Sort Algorithm ####

# Time Complexity: O(N^2)
# Auxiliary Complexity: O(1) as the only extra memory used is for temporary variables while swapping two values in Array.

#### Algorithm Explanation ####

# Bubble Algorithm swap the adjacent elements if previous index value is greater than next index value.
# Thus is puts the max value at the end of the array
# start from the first index and compare with second index. if first > second, then swap continue for the rest of the indexes
# thus after first iteration last two indexes are the greatest
# after second iteration last three indexes are the greatest
# and continue the process

arr = list(map(int, input().split()))

for i in range(len(arr)):
    # Last i elements are already in place
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)