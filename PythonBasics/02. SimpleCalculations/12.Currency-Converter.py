value = float(input())
firstCurrancy = input()
wantedCurrancy = input()

inLevs = None

if firstCurrancy == "USD":
    inLevs = value * 1.79549
elif firstCurrancy == "EUR":
    inLevs = value * 1.95583
elif firstCurrancy == "GBP":
    inLevs = value * 2.53405
else:
    inLevs = value

inWantedCurrancy = None

if wantedCurrancy == "USD":
    inWantedCurrancy = inLevs / 1.79549
elif wantedCurrancy == "EUR":
    inWantedCurrancy = inLevs / 1.95583
elif wantedCurrancy == "GBP":
    inWantedCurrancy = inLevs / 2.53405
else:
    inWantedCurrancy = inLevs

print("{0:.2f} {1}".format(inWantedCurrancy, wantedCurrancy))


