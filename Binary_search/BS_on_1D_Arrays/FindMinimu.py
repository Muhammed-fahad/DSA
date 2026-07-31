# Find Minimum in rotated sorted array
def RotatedSortedArray(arr):
    low, high = 0 , len(arr)-1
    ans = 1000
    while(low <= high):
        mid = (low+high) // 2
        if(arr[low] < arr[mid]):
            ans = min(ans, arr[low])
            low = mid+1
        else:
            ans = min(ans , arr[mid])
            high = mid-1
    return ans

if __name__ == "__main__":
    arr = [4,5,6,1,2,3,4]
    print(RotatedSortedArray(arr))