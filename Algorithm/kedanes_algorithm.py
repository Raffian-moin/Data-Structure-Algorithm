#--------------
# Overview
#---------------
"""
Kedane's algorithm is used to find largest sum of the sub-array.
we keep track of the maximum sum of the sub-array ending at current position.
if current element is greater than sub-array ending at current position we take
current element as maximum else take sub-array sum ending at current position.
then compare current maximum with all other maximum sums and update the value
"""
#--------------
# Limitations
#---------------
"""
Kadane's Algorithm assumes that the array contains at least one positive value. 
If the array contains only negative values, the algorithm will return 0 as 
the maximum sub-array sum, which may not be the desired result.
"""

a = list(map(int, input().split()))
localMax = 0
globalMax = 0

for el in a:
    localMax = max(el, localMax+el)
    if localMax > globalMax:
        globalMax = localMax

print(globalMax)