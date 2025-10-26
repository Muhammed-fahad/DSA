def sort_brutefoce(arr):
    return sorted(arr)

def sort_better(arr):
    zero = one = two = 0
    
    # Count the number of 0s, 1s, and 2s
    for i in arr:
        if i == 0:
            zero += 1
        elif i == 1:
            one += 1
        else:
            two += 1

    # Fill the array with counted values
    for j in range(zero):
        arr[j] = 0

    for k in range(zero, zero + one):
        arr[k] = 1

    for l in range(zero + one, zero + one + two):
        arr[l] = 2
    
    return arr



arr = [0 ,1 , 1, 2, 0, 2, 1, 1, 0]
print(sort_brutefoce(arr))
print(sort_better(arr))