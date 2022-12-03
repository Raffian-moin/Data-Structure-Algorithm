array = list(map(int, input().split()))

start = 0
end = len(array)-1
for i in range(len(array)-1):
    if start < end:
        array[start], array[end] = array[end], array[start]
        start = start+1
        end = end-1

print(array)
