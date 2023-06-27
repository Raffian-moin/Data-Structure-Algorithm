"""
Given an array arr[], an integer K and a Sum. 
The task is to check if there exists any subarray with K elements whose sum is equal to the given sum. 
If any of the subarray with size K has the sum equal to the given sum then print YES otherwise print NO.
"""
# source
# https://www.geeksforgeeks.org/subarray-of-size-k-with-given-sum/

#-------------------------------------------
# solution using sliding window technique
#-------------------------------------------

a=list(map(int, input().split()))
k,s=list(map(int, input().split()))
m=0
for i in range(len(a)):
    m+=a[i]
    if i+1>k:
        m-=a[i-k]

    if m==s:
        print('YES')
        break
else:
    print('NO')

