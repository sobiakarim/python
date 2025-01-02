n = int(input("Total elements of list: "))
print(f"Enter {n} digits for list1: " )
l1 = [int(input()) for _ in range(n)]

print(f"Enter {n} digits for list2: " )
l2 = [int(input()) for _ in range(n)]

l3 = [0] * n

for i in range(n):
    l3[i] = l1[i]+l2[i]

print(f"List 3: {l3}")    