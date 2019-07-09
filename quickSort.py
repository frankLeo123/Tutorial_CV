def quickSort(arr):
    if len(arr) <= 1:
        return arr
    flag = len(arr) // 2
    left = [x for x in arr if x < arr[flag]]
    middle = [x for x in arr if x == arr[flag]]
    right = [x for x in arr if x > arr[flag]]

    return quickSort(left) + middle + quickSort(right)

print(quickSort([1,2,3,9,2,6,1]))