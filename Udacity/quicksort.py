"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array)-1]
    leftArr = []
    rightArr = []
    
    for i in array[:len(array)-1]:
        if i > pivot:
            rightArr.append(i)
        elif i <= pivot:
            leftArr.append(i)
        
    leftArr = quicksort(leftArr)
    rightArr = quicksort(rightArr)
    
    leftArr.append(pivot)
    sortedArr = leftArr + rightArr

    return sortedArr

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))