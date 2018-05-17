import math

year_type = input().lower()
holidays_in_year = int(input())
weekends_in_home_town = int(input())

weekends_in_Sofia = 48 - weekends_in_home_town
saturday_plays = (3.0 / 4) * weekends_in_Sofia
holiday_plays = (2.0 / 3) * holidays_in_year

total_plays = saturday_plays + holiday_plays + weekends_in_home_town

if year_type == "leap":
    total_plays += 0.15 * total_plays

print("{0}".format(math.floor(total_plays)))
