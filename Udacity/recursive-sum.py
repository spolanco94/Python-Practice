def sum(arr):
    if len(arr) == 0:
        total = 0
    elif len(arr) == 1:
        total = arr[0]
    else:
        total= arr[0] + sum(arr[1:])

    return total

array = [2, 4, 6]
print(sum(array))

def count(list):
    if len(list) == 0:
        total = 0
    elif len(list) == 1:
        total = 1
    else:
        total= 1 + count(list[1:])

    return total

array2 = ["apples", "bananas", "pineapples", "kiwi", "mangoes"]
print(count(array2))

def findMax(nums):
    if len(nums) == 0:
        max = None
    elif len(nums) == 1:
        max = nums[0]
    else:
        if nums[0] > nums[1]:
            nums.pop(1)
        else:
            nums.pop(0)
        max = findMax(nums)

    return max

array3 = [12, 36, 36, 3, 9, 28, 90]
# print(findMax(array3)) 
print(array3[:-2])
