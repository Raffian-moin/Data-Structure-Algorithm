def sortedArray(arr, index):
    if index == len(arr)-1:
        print('sorted')
        return
    
    if arr[index+1] >= arr[index]:
        sortedArray(arr, index+1)
    else:
        print('not sorted')
        return
    
sortedArray([1, 2, 4, 3], 0)