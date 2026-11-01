def MaxSubArray_Bruteforce(arr):
    # Generate all the subarray
    maxsum = float('-inf')
    for i in range(len(arr)):
        val = 0
        for j in range(i,len(arr)):
            val += arr[j]
            maxsum = max(val,maxsum)
    return maxsum

def MaxSubArray_Optimal(arr):
    Maxsum = float('-inf')
    val = 0
    for i in range(len(arr)):
        val += arr[i]
        Maxsum = max(val,Maxsum)
        if val < 0:
            val = 0
    return Maxsum


if __name__ == "__main__":
    arr = [-2,-3,4,-1,-2,1,5,-3]
    print(MaxSubArray_Bruteforce(arr))
    print(MaxSubArray_Optimal(arr))
