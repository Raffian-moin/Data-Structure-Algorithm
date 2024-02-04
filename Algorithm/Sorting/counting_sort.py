#### Counting Sort Algorithm ####

#### Time and Space Complexity ####
"""
Time Complexity: O(log(N + M))
Auxiliary Complexity: O(log(N + M)) as we take array of length N for output
and array of length M for countArray
"""

#### Algorithm Explanation ####
"""
Counting Sort Algorithm is a non-comparison counting based stable algorithm.
We first take the maximum value of array and create an array of length of
maximum_value + 1. why? because we will store the frequency of each element
of the array in the countArray. where element frequency is stored in
countArray[element_value] = element_frequency.

Then we will store the prefix sum of the countArray. why? As we have stored
the frequency of the each element, if element 1 has two frequency then both of
them will take the first and second place in the output array. and if 2 has 3 frequency,
then they will take 3, 4, and 5th position in output array.

Next we iterate over the input array and and find its position from the prefix-sum
array and put that element in that position-1 (for prefix sum array count
start from 1 but our output array index start from 1), and decrement that elements
count by 1 from prefix sum array. then if that element is again encountered then that element
will be placed previous position of that same element. And keep repeating the process
until we reach the first element.
"""

arr = list(map(int, input().split()))

length = len(arr)

countArray = [0] * (max(arr) + 1)

outputArray = [0] * length

for i in range(length):
    countArray[arr[i]] +=1

for i in range(1, len(countArray)):
    countArray[i] += countArray[i - 1]

for i in range(length - 1, -1, -1):
    outputArray[countArray[arr[i]] -1 ] = arr[i]
    countArray[arr[i] ] -=1

print(outputArray)