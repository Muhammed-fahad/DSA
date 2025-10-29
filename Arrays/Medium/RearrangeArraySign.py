# we have an array of positive and negative integers
# we have to rearrange the array in such a way that positive and negative integers are placed alternatively

def rearrange_array_sign(arr):
    positive = []
    nefative = []
    for i in arr:
        if i >= 0:
            positive.append(i)
        else:
            nefative.append(i)
    
    result = [0]*len(arr)
    for i in range(len(arr)//2):
        result[i*2] = positive[i]
        result[i*2 + 1] = nefative[i]  
    return result

print(rearrange_array_sign([3, -2, 5, -1, -7, 4, -3, 6]))

def rearrange_better(arr):
    result = [0]*len(arr)
    posIndex = 0
    negIndex = 1
    for i in arr:
        if i >= 0:
            result[posIndex] = i
            posIndex += 2
        else:
            result[negIndex] = i
            negIndex += 2
    return result 
print(rearrange_better([3, -2, 5, -1, -7, 4, -3, 6]))

# if the positive and negative are not equal in number
def rearrange_general(arr):
    positive = []
    nefative = []
    for i in arr:
        if i >= 0:
            positive.append(i)
        else:
            nefative.append(i)
    
    result = []
    i = 0
    j = 0
    while i < len(positive) and j < len(nefative):
        result.append(positive[i])
        result.append(nefative[j])
        i += 1
        j += 1
    
    while i < len(positive):
        result.append(positive[i])
        i += 1
    
    while j < len(nefative):
        result.append(nefative[j])
        j += 1
    
    return result