n = int(input())

max_diff = 0
last_pair_sum = 0

for i in range(0, n):
    num1 = int(input())
    num2 = int(input())

    current_sum = num1 + num2

    if i == 0:
        last_pair_sum = current_sum

    current_diff = abs(current_sum - last_pair_sum)

    if current_diff > max_diff:
        max_diff = current_diff

    last_pair_sum = current_sum

if max_diff == 0:
    print("Yes, value={0}".format(last_pair_sum))
else:
    print("No, maxdiff={0}".format(max_diff))

