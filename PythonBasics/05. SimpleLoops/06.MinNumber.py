n = int(input())

min = float('inf')

for i in range(0, n):
    num = int(input())

    if num < min:
        min = num

print(min)
