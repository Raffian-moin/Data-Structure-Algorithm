#### Selection Algorithm ####

# Time Complexity: O(N^2)
# Auxiliary Complexity: O(1) as the only extra memory used is for temporary variables while swapping two values in Array.

#### Algorithm Explanation ####

# Selection Algorithm search for the minimum and place the value at the beginning of the array
# start from the first index and assume it's the minimum value then compare with all other indexes if minimum value is
# found in other indexes then swap value of first index and minimum value index. now first item is sorted.
# then repeat the process for 2,3...n indexes

arr = list(map(int, input().split()))

for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print(*arr)
            