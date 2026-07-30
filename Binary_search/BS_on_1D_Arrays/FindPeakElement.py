def FindPeak(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return arr[low]


arr = [4,5,6,7,3,2,1]
print(FindPeak(arr))