def FindCommponPrefix(str):
    ans = ""
    str.sort()
    first,last= str[0],str[-1]
    for i in range(min(len(first) , len(last))):
        if first[i] != last [i]:
            return ans
        ans+=first[i]
    return ans

if __name__ == "__main__":
    input_strs = ["interview", "internet", "internal", "interval"]
    print(FindCommponPrefix(input_strs))
