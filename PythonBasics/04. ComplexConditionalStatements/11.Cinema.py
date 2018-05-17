film_type = input().lower()
rows = int(input())
cols = int(input())

total_seats = rows * cols

price_Of_Billet = 0.0

if film_type == "premiere":
    price_Of_Billet = 12.0
elif film_type == "normal":
    price_Of_Billet = 7.50
elif film_type == "discount":
    price_Of_Billet = 5.0

money_earned = price_Of_Billet * total_seats

print("{0:.2f} leva".format(money_earned))
