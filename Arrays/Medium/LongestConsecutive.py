arr = [102,4,100,1,101,3,2,1,1,5]
def LongestConsecutive(arr):
    value = 0
    for i in arr:
        num = 1
        a = i
        while(True):
            if(a+1 in arr):
                num+=1
                a+=1
            else:
                value = max(num,value)
                break
    return value
print(LongestConsecutive(arr))



def LongestConsecutive_Better(arr):
    arr = sorted(set(arr))
    maxi = 0
    value = 1
    for i in range(len(arr)-1):
        if(arr[i+1] == arr[i]+1):
            value+=1
        else:
            maxi = max(maxi,value)
            value = 1
    return maxi

print(LongestConsecutive_Better(arr))
        