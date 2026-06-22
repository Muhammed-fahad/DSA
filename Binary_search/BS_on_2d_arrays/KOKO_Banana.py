import math
def hour_found(arr,n):
    total_hour = 0
    for banana in arr:
        total_hour += math.ceil(banana/n)
    return total_hour

def KokoBanana():
    piles = [3,6,7,11]
    h = 8 # This is the maximum hour , we need to find what is the minimum number of banana it can eat under this time to complete 
    high = max(piles)
    low  = 1
    while low <= high:
        mid = math.ceil((low+high)/2)
        value = hour_found(piles,mid)
        if(value <= h):
            high = mid-1
        else:
            low = mid+1
    return low

if __name__ == "__main__":
    print(KokoBanana())