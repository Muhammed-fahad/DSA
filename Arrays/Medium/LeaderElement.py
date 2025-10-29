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


def find_leader_optimal(arr):
    leader = []
    maxi = float('-inf')
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > maxi:
            maxi = arr[i]
            leader.append(maxi)
    return leader[::-1]

print(find_leader_optimal(arr))