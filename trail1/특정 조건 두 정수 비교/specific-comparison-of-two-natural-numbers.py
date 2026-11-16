arr = input().split()

a = int(arr[0])
b = int(arr[1])

if a < b:
    x = 1
else:
    x = 0

if a == b:
    y = 1
else:
    y = 0

print(f"{x} {y}")