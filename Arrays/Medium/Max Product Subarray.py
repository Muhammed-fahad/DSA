def MaxProductSubArray_bruteforce(arr):
    maxvalue = float('-inf')
    for i in range(len(arr)):
        product = 1
        for j in range(i,len(arr)):
            product*=arr[j]
            maxvalue = max(product,maxvalue)
    return maxvalue

def MaxProductSubarray_optimal(arr):
    pref , suff = 1,1
    maxvalue = float('-inf')
    for i in range(len(arr)):
        if pref == 0:
            pref = 1
        if suff == 0:
            suff = 1
        
        pref*=arr[i]
        suff*arr[len(arr)-i-1]
        maxvalue = max(maxvalue,max(pref,suff))
    return maxvalue

if __name__ == "__main__":
    arr = [2,3,-2,4]
    #print(MaxProductSubArray_bruteforce(arr))
    print(MaxProductSubarray_optimal(arr))
