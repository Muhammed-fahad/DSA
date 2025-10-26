arr = [13, 46, 24, 56 , 20 , 9]
for i in range(len(arr)):
    mini = min(arr[i:len(arr)+1])
    index1 = arr.index(mini)
    arr[i] , arr[index1] = mini , arr[i]
print(arr)