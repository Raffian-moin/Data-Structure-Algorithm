# Problem Source: https://www.enjoyalgorithms.com/blog/count-distinct-elements-in-every-window

# Problem:
# Count Distinct Elements in Every k Size Window

# Problem Statement:
# You are given an array X[] of size n and an integer k, 
# write a program to count the distinct elements present in every k sized window 
# of the array. 

from collections import defaultdict 

arr = list(map(int, input().split()))
k = int(input())

frequency = defaultdict(int) 
count = 0
result = []
j = 0

for j in range(k):
    frequency[arr[j]] +=1
    if frequency[arr[j]] == 1:
        count +=1
        
result.append(count)

for i in range(k, len(arr)):

    frequency[arr[i-4]] -=1
    if frequency[arr[i-4]] ==0:
        count -=1

    frequency[arr[i]] +=1
    if frequency[arr[i]] == 1:
        count +=1

    result.append(count)

print(result)