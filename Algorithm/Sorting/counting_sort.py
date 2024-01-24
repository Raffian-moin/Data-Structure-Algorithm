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