# In a Array , an element is called a "leader" if it is greater than all the elements to its right side.

def find_leaders(arr):
    leader = []
    for i in range(len(arr)):
        flag = True
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                flag = False
                break
        if(flag):
            leader.append(arr[i])
    return leader
            

arr = [10,22,12,3,0,6]
print(find_leaders(arr))


