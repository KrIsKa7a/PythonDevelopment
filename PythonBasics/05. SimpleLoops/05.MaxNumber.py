import sys

n = int(input())

max = float('-inf')

for i in range(0, n):
    num = int(input())

    if num > max:
        max = num

print(max)

