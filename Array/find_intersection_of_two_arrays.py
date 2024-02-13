arr1 = [1, 2, 3, 4, 5, 5, 5]
arr2 = [1, 1, 2, 2, 5, 5, 6, 6, 6, 4, 4, 4]
arr1.sort()
arr2.sort()
result = []
i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
        if len(result) == 0 or (len(result) and result[-1] != arr1[i]):
            result.append(arr1[i])
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        i += 1
    elif arr1[i] > arr2[j]:
        j += 1

print(result)