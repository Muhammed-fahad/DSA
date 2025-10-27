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