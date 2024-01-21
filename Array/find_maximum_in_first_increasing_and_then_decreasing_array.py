arr = list(map(int, input().split()))
l = 0
r = len(arr) - 1

while True:
    
    mid = l + (r-l)//2

    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        print(arr[mid])
        break
    elif arr[mid] > arr[mid-1]:
        l = mid+1
    elif arr[mid] < arr[mid-1]:
        r = mid-1

