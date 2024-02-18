arr = [10, 21, 22, 100, 101, 200, 300]
arr.sort()

count = 0

for i in range(len(arr) - 1, 1, -1):
    l = 0
    r = i - 1

    while l < r:
        if arr[l] + arr[r] > arr[i]:
            count += r - l
            r -= 1
        else:
            l += 1

print(count)

