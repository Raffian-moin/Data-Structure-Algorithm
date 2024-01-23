arr = [5, 11, 13, 5, 6, 7]

def mergeSort(arr):

    if len(arr) > 1:

        mid = len(arr)//2

        leftHalf = arr[:mid]

        rightHalf = arr[mid:]

        mergeSort(leftHalf)

        mergeSort(rightHalf)

        i, j, k = 0, 0, 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i +=1
            else:
                arr[k] = rightHalf[j]
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
print("Sorted Array:", arr)
