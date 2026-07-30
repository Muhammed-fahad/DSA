def LowerBound(arr , target):
    low , high = 0 , len(arr)-1
    ans = -1
    while(low <= high):
        mid = (low+high)//2
        if(target <= arr[mid]):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

def UpperBound(arr, target):
    low , high = 0 , len(arr) -1
    ans = -1
    while (low <= high):
        mid = (low+high) //2 
        if(target < arr[mid]):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
    

if __name__ == "__main__":
    arr = [1,2,3,4,4,4,5,8,9]
    target = 4
    print (UpperBound(arr,target) - LowerBound(arr, target))
