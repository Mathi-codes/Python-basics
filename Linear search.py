def Linear_search(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1
array=list(map(int, input("Enter the elements (comma - seperated : ").split()))
target=int(input("Enter the target : "))
print(Linear_search(array,target))