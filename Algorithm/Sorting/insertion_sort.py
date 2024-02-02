#### Insertion Sort Algorithm ####

#### Time and Space Complexity ####
"""
Time Complexity: O(N^2)
Auxiliary Complexity: O(1) as the only extra memory used is for temporary variables while swapping two values in Array.
"""


#### Algorithm Explanation ####
"""
We pick an element and check if it is smaller than it's left element.
If it is smaller then we swap the elements and keep doing this until
we find elements that are less than current element or we reach the
first element.
Thus the smaller element is in it's correct position.
We do this for all elements.
Imagine we have two deck of cards in our two hands.
we take one card from the deck of right hand and put
it in it's correct position in the deck of left hand.
"""

arr = list(map(int, input().split()))

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j+1] = key

print(*arr)