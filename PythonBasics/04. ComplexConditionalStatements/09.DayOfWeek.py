number_of_the_day = float(input())

days_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

if number_of_the_day in days_of_week:
    print(days_of_week[number_of_the_day])
else:
    print("Error")
