arr = [6, 3, 1, 5, 10, 2, 4]

length = len(arr)

k = 7

def swap(low, high):
    i = low
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[j], arr[i] = arr[i], arr[j]
    return i

def partition(low, high):

    pi = swap(low, high)

    if pi == length - k:
        return
    elif pi < length - k:
        pi = swap(pi + 1, high)
    else:
        pi = swap(low, pi - 1)




partition(0, length - 1)

print(arr[length - k])