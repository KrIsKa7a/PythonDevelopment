n = int(input())

left_sum = 0
right_sum = 0

for i in range(0, 2 * n):
    num = int(input())

    if i < n:
        left_sum += num
    else:
        right_sum += num

if left_sum == right_sum:
    print("Yes, sum = {0}".format(left_sum))
else:
    print("No, diff = {0}".format(abs(left_sum - right_sum)))

