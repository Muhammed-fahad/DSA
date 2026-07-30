# Find how many time rotated 
def HowManyTimeRotated(arr):
    low, high = 0 , len(arr)-1
    ans = 1000
    index = -1
    while(low <= high):
        mid = (low+high) // 2

        if(arr[low] < arr[mid]):
            if(arr[low] < ans):
                ans = arr[low]
                index = low
            low = mid+1
        else:
            if(arr[mid] < ans):
                ans = mid
                index = mid
            high = mid-1

    return index

if __name__ == "__main__":
    arr = [4,5,6,1,2,3,4]
    print(HowManyTimeRotated(arr))