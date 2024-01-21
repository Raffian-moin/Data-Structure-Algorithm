# Problem Source: https://www.enjoyalgorithms.com/blog/check-for-pair-in-an-array-with-a-given-sum

# Problem:
# Check for pair in an array with a given sum


arr = list(map(int, input().split()))
targetSum = 15

# Two pointer approach
arr.sort()

i = 0
j = len(arr) - 1
while j > i:
    if arr[i] + arr[j] > targetSum:
        j -=1
    elif arr[i] + arr[j] < targetSum:
        i +=1
    else:
        print("True")
        break
else:
    print("False")

# Hash map approach
s = set()

for el in arr:
    if (targetSum - el) in s:
        print("True")
        break
    s.add(el)
else:
    print("False")