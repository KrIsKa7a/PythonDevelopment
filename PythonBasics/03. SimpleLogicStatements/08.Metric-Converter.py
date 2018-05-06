value = float(input())
given = input()
wanted = input()

inMeters = None

if given == "m":
    inMeters = value
elif given == "mm":
    inMeters = value / 1000
elif given == "cm":
    inMeters = value / 100
elif given == "mi":
    inMeters = value / 0.000621371192
elif given == "in":
    inMeters = value / 39.3700787
elif given == "km":
    inMeters = value / 0.001
elif given == "ft":
    inMeters = value / 3.2808399
elif given == "yd":
    inMeters = value / 1.0936133

inWanted = None

if wanted == "m":
    inWanted = inMeters
elif wanted == "mm":
    inWanted = inMeters * 1000
elif wanted == "cm":
    inWanted = inMeters * 100
elif wanted == "mi":
    inWanted = inMeters * 0.000621371192
elif wanted == "in":
    inWanted = inMeters * 39.3700787
elif wanted == "km":
    inWanted = inMeters * 0.001
elif wanted == "ft":
    inWanted = inMeters * 3.2808399
elif wanted == "yd":
    inWanted = inMeters * 1.0936133

print("{0} {1}".format(inWanted, wanted))

