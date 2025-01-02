n = int(input("Total elements of list: "))
print(f"Enter {n} digits for list1: " )
list1 = [int(input()) for _ in range(n)]

print(f"Enter {n} digits for list2: " )
list2 = [int(input()) for _ in range(n)]

list3 = [0] * n

for i in range(n):
    list3[i] = list1[i]+list2[i]

print(f"List 3: {list3}")    