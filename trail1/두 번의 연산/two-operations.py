A = int(input())

if A % 2 != 0:
    A = int(A+3)

if A % 3 == 0:
    A = int(A/3)

print(A)