import sys
"""
Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in the array
"""
#------------
# METHOD: 1
# We will use Set(). Since set removes the duplicate elements, 
# if there is only one element in the set then second largest doesn't exist. \
# otherwise return second element from the end.
#-------------
arr=[12, 35, 1, 10, 34, 1]
s=set(arr)
print(s)
if len(s)==1:
    print('Second largest element dont exist')
else:
    print(sorted(list(s))[-2])

#------------
# METHOD: 2
# We will use two variables to store largest and second largest elements
# Initialize two variables (first, second) to smallest values. then traverse the array from left to right.
# If current element is greater than first assign first=current and second=first
# If current element grater than
#-------------

arr=[12, 35, 1, 10, 34, 1]
first=-sys.maxsize
second=-sys.maxsize
for el in arr:
    second=max(min(first, el), second)
    if el>first:
        first=el

if second==first:
    print('Second largest element dont exist')
else:
    print(second)
#--------------------------------
# When not to use METHOD: 2
#--------------------------------

# If we are asked to largest n number we need to maintain n variables.
# In that case it's not effective