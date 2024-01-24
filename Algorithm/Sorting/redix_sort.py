arr = list(map(int, input().split()))

def countSort(arr, place):
    arrSize = len(arr)
    count = [0] * 10
    output = [0] * arrSize

    for i in range(arrSize):
        index = arr[i] // place
        count[index % 10] +=1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(arrSize-1, -1, -1):
        index = arr[i] // place
        output[count[index % 10] -1] = arr[i]
        count[index % 10] -=1

    for i in range(arrSize):
        arr[i] = output[i]

def radixSort(arr):

    maxElement = max(arr)

    place = 1

    while maxElement // place > 0:
        countSort(arr, place)
        place *= 10


radixSort(arr)    

print(arr)