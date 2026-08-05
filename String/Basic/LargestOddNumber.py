def LargestOddNumber(word):
    ind = len(word)-1
    for i in range(ind,-1,-1):
        if(int(word[i]) % 2 == 1):
            ind = i
            break
    
    if ind == -1:
        return ""
    
    i = 0 
    while(i<=ind and int(word[i]) == 0):
        i+=1
    return word[i:ind+1]

if __name__ == "__main__":
    word = input("Enter a string: ")
    print(LargestOddNumber(word))