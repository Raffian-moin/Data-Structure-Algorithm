def binarySearch(start, end):
    mid = start + (end-start) // 2
    if start > end:
        print('not found')
        return
    
    if arr[mid] == find:
        print('found in position: ', mid)
        return
    elif arr[mid] > find:
        return binarySearch(start, mid-1)
    elif arr[mid] < find:
        return binarySearch(mid+1, end)
    

arr = [1, 2, 3, 5, 6, 7]
start = 0
end = len(arr)-1
find = -1
binarySearch(start, end)