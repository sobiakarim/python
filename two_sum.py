'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

target = int(input("Target = \n"))
n = int(input("Total number of elements in input array: \n"))
print(f"Enter {n} numbers: ")
arr = [int(input()) for _ in range(n)]
found = False

for i in range(n):
    if not found:
        for j in range(n):
            if i==j:
                continue

            if arr[i]+arr[j]==target:
                print(f"[ {i} , {j}]")
                found= True
                break
