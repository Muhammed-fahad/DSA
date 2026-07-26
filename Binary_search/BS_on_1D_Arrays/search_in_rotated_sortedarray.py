def rotatedsortedarray(arr,target):
    low , high = 0 , len(arr)-1
    while(low <= high):
        mid = (low+high)//2
        if(arr[mid] == target):
            return mid
        
        elif(arr[low] <= arr [mid]):
            if(arr[low] <= target < mid):
                high = mid -1
            else:
                low = mid+1
        else:
            if(arr[mid] < target <= high):
                low = mid+1
            else:
                high = mid-1
    return -1


if __name__ == "__main__":
    arr = [4,5,6,7,7,7,0,1,2]
    target = 0
    print(rotatedsortedarray(arr,target))