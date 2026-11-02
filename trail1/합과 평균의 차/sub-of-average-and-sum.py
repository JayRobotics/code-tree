a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

s = a+b+c
avg = int((a+b+c)/3)

print(f"{s}")
print(f"{avg}")
print(f"{int(s-avg)}")