import datetime

date = datetime.datetime.strptime(input(), "%d-%m-%Y")

dateWanted = date + datetime.timedelta(days=999)

print(dateWanted.strftime("%d-%m-%Y"))

