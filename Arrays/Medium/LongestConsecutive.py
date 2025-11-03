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


def longestSuccessiveElements_optmal(a):
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set()
    # put all the array elements into set
    for i in range(n):
        st.add(a[i])

    # Find the longest sequence
    for it in st:
        # if 'it' is a starting number
        if it - 1 not in st:
            # find consecutive numbers
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements_optmal(a)
print("The longest consecutive sequence is", ans)