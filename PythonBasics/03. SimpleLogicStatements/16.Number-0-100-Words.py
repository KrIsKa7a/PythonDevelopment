number = int(input())

if number < 0 or number > 100:
    print("invalid number")
else:
    if number == 100:
        print("one hundred")
    else:
        numbersZeroToTwelve = []
        numbersZeroToTwelve[0:12] = \
            ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
        numbersThirteenToNineTeen = []
        numbersThirteenToNineTeen[0:7] = \
            ["thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        numbersPrefixs = []
        numbersPrefixs[0:8] = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        if number >= 0 and number <= 12:
            print(numbersZeroToTwelve[number])
        elif number >= 13 and number <= 19:
            print(numbersThirteenToNineTeen[number - 13])
        else:
            numberToStr = str(number)

            if numberToStr[1] == "0":
                print(numbersPrefixs[int(numberToStr[0]) - 2])
            else:
                print(numbersPrefixs[int(numberToStr[0]) - 2] + " " + numbersZeroToTwelve[int(numberToStr[1])])

