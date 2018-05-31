n = int(input())

odd_sum = 0
odd_min = "No"
odd_max = "No"
even_sum = 0
even_min = "No"
even_max = "No"

for i in range(1, n + 1):
    currentNum = float(input())

    if i == 1:
        odd_min = currentNum
        odd_max = currentNum
    elif i == 2:
        even_min = currentNum
        even_max = currentNum

    if i % 2 == 0:
        even_sum += currentNum

        if currentNum > even_max:
            even_max = currentNum
        elif currentNum < even_min:
            even_min = currentNum
    else:
        odd_sum += currentNum

        if currentNum > odd_max:
            odd_max = currentNum
        elif currentNum < odd_min:
            odd_min = currentNum

print("OddSum={0},".format(odd_sum))
print("OddMin={0},".format(odd_min))
print("OddMax={0},".format(odd_max))
print("EvenSum={0},".format(even_sum))
print("EvenMin={0},".format(even_min))
print("EvenMax={0}".format(even_max))
