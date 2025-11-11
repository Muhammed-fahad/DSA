# a
# 2 b
# c 3 c
# 4 d 4 d
# e 5 e 5 e

n = int(input("Enter the number: "))

for i in range(1,n+1):
    # for even line
    if(i%2 == 0):
        flag1 = True # for num , false for char
        print()
        for j in range(i):
            if(flag1):
                print(i , end= " ")
                flag1 = False
            else:
                print (chr(i+96) , end= " ")
                flag1 = True
        
    
    # for odd line
    else:
        flag2 = True # for char . false for num
        print()
        for j in range(i):
            if(flag2):
                print(chr(i+96) , end= " ")
                flag2 = False
            else:
                print (i , end= " ")
                flag2 = True