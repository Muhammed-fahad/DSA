from itertools import combinations

def allsubarray(arr):
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            subarray = arr[i:j+1]
            result.append(subarray)
    return result
print(allsubarray([1, 2, 3]))

def allsubarray_optimal(arr):
    result = []
    n = len(arr)
    for i in range(n):
        subarray = []
        for j in range(i, n):
            subarray.append(arr[j])
            result.append(subarray.copy())
    return result
print(allsubarray_optimal([1, 2, 3]))

def allsubarray_BitMaskSolution(arr):
    n = len(arr)
    result = []
    for i in range(1<<n):
        temp = []
        for j in range(n):
            if i & (1<<j):
                temp.append(arr[j])
        result.append(temp)
    return result

print(allsubarray_BitMaskSolution([1,2,3]))

def subarray_inbuil(arr):
    result = []
    for i in range(len(arr)+1):
        result.append(list(combinations(arr,i)))
    return result
print(subarray_inbuil([1,2,3]))