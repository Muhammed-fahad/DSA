def UpperBound(arr,target):
    low,high = 0, len(arr)-1
    ans = len(arr)

    while low <= high:
        mid = (low+high)// 2
        if (target < arr[mid]):
            high = mid -1
            ans = mid
        else:
            low = mid+1
    return ans

if __name__ == "__main__":
    arr = [1,2,3,4,4,4,5,8,9]
    target = 5
    print(UpperBound(arr,target))