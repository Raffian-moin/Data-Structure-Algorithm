arr = [1, 20, 6, 4, 5]
count = 0

def mergeSort(arr):
    global count
    if len(arr) > 1:

        mid = len(arr)//2

        leftHalf = arr[:mid]

        rightHalf = arr[mid:]

        mergeSort(leftHalf)

        mergeSort(rightHalf)

        i, j, k = 0, 0, 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                arr[k] = leftHalf[i]
                i +=1
            else:
                arr[k] = rightHalf[j]
                count += len(leftHalf) - k + j
                j +=1
            k +=1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i +=1
            k +=1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j +=1
            k +=1



print("Unsorted Array:", arr)
mergeSort(arr)
print(count)
