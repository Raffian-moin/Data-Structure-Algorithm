def linearSearch(arr, index):
    if arr[index] == target:
        print('Found at position: ', index)
        return index
    elif index == len(arr)-1:
        print('Not found')
        return

    linearSearch(arr, index+1)

target = 6
linearSearch([1, 2, 3, 4], 0) 