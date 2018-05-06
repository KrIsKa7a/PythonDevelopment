number = int(input())

numbersToText = []
numbersToText[0:9] = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

try:
    print(numbersToText[number])
except IndexError:
    print("number too big")

