# Find the Square root of the number it should be whole number 
def FindSuareRootNo(number):
    low,high = 0,number//2
    ans = 0
    while(low <= high):
        mid = (low+high)//2
        if(mid*mid <= number):
            ans = mid
            low = mid+1
        else:
            high = mid -1 
    return ans
if __name__ == "__main__":
    findroot = 37
    print(FindSuareRootNo(findroot))