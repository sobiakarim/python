n = int(input("Total elements of list: "))
print(f"Enter {n} digits for list1: " )
list1 = [int(input()) for _ in range(n)]
print(f"Enter {n} digits for list2: " )
list2 = [int(input()) for _ in range(n)]
list3 = [0] * n
for i in range(n-1, -1, -1):
    list3[i] = list1[i]+list2[i]
    if list3[i]>9:
        if i > 0:
            remainder = list3[i]%10
            quotient = list3[i]//10
            list3[i]=remainder
            list1[i-1]=list1[i-1]+quotient
        

print(f"List 3: {list3}")    