n = int(input())

numbers = [None] * n

for i in range(0, n):
    num = int(input())

    numbers[i] = num

max = float('-inf')
sum = 0

for i in range(0, n):
    current_num = numbers[i]

    if current_num > max:
        max = current_num

    sum += current_num

sum -= max

if sum == max:
    print("Yes")
    print("Sum = {0}".format(sum))
else:
    print("No")
    print("Diff = {0}".format(abs(sum - max)))

