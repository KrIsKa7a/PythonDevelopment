name_given = input().lower()

fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetables = ["tomato", "cucumber", "pepper", "carrot"]

if name_given in fruits:
    print("fruit")
elif name_given in vegetables:
    print("vegetable")
else:
    print("unknown")
