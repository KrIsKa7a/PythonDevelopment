product = input().lower()
town = input().lower()
quantity = float(input())

prices = None

if town == "sofia":
    prices = {
        "coffee": 0.50,
        "water": 0.80,
        "beer": 1.20,
        "sweets": 1.45,
        "peanuts": 1.60
    }
elif town == "plovdiv":
    prices = {
        "coffee": 0.40,
        "water": 0.70,
        "beer": 1.15,
        "sweets": 1.30,
        "peanuts": 1.50
    }
elif town == "varna":
    prices = {
        "coffee": 0.45,
        "water": 0.70,
        "beer": 1.10,
        "sweets": 1.35,
        "peanuts": 1.55
    }

if product in prices:
    bill = prices[product] * quantity

    print("{0:.2f}".format(bill))
else:
    print("Product not found in our price list!")

