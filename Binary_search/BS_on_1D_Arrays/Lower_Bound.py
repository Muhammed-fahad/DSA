def LowerBound(arr,target):
    ans = len(arr)
    low,high = 0,len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if(arr[mid] >= target):
            ans = mid 
            high = mid-1
        else:
            low = mid+1
    return ans


if __name__ == "__main__":
    arr = [1,2,3,4,4,4,5,8,9]
    target = 4
    print(LowerBound(arr,target))