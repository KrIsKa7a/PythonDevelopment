number = int(input())

bonusPoints = None

if number <= 100:
    bonusPoints = 5
elif number > 100 and number <= 1000:
    bonusPoints = 0.20 * number
elif number > 1000:
    bonusPoints = 0.10 * number

if number % 2 == 0:
    bonusPoints += 1
elif number % 5 == 0:
    bonusPoints += 2

print(bonusPoints)
print(number + bonusPoints)
