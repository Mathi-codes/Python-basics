def binarysearch(array, low, high, target):
    if high >= low:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binarysearch(array, mid + 1, high, target)
        else:
            return binarysearch(array, low, mid - 1, target)
    else:
        return -1

array = list(map(int, input("Enter space-separated sorted array elements: ").split()))
target = int(input("Enter the target: "))
print(binarysearch(array, 0, len(array) - 1, target))
