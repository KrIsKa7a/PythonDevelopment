product = input().lower()
day = input().lower()
quantity = float(input())

workDays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
holidays = ["saturday", "sunday"]

prices = {}
has_error = False

if day in workDays:
    prices = {
        "banana": 2.50,
        "apple": 1.20,
        "orange": 0.85,
        "grapefruit": 1.45,
        "kiwi": 2.70,
        "pineapple": 5.50,
        "grapes": 3.85
    }
elif day in holidays:
    prices = {
        "banana": 2.70,
        "apple": 1.25,
        "orange": 0.90,
        "grapefruit": 1.60,
        "kiwi": 3.00,
        "pineapple": 5.60,
        "grapes": 4.20
    }
else:
    has_error = True

if not product in prices:
    has_error = True

if has_error:
    print("Error")
else:
    bill = prices[product] * quantity
    print("{0:.2f}".format(bill))
