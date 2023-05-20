a=[10, 4, 3, 50, 23, 90]
first = -10000000
second = -10000000
third = -10000000

for element in a:
    if element > first:
        third, second, first = second, first, element
    elif element < first and element > second:
        third, second = second, element
    elif element > third:
        third = element

print(first, second, third)

#---------------------------------
# When not to use this approach:
#---------------------------------

# This approach is not an efficient solution because if we are asked to
# find the largest n elements we need to maintain n variables to store
# and compare elements which is cumbersome.

#--------------------
# Better solution:
#--------------------

# It is best to sort the array using O(n log n) algorithm and return the last n elements