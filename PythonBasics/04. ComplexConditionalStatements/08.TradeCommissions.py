town = input().lower()
sales = float(input())

commissions = {}
has_errors = False

if sales >= 0 and sales <= 500:
    commissions = {
        "sofia": 0.05,
        "varna": 0.045,
        "plovdiv": 0.055
    }
elif sales > 500 and sales <= 1000:
    commissions = {
        "sofia": 0.07,
        "varna": 0.075,
        "plovdiv": 0.08
    }
elif sales > 1000 and sales <= 10_000:
    commissions = {
        "sofia": 0.08,
        "varna": 0.10,
        "plovdiv": 0.12
    }
elif sales > 10_000:
    commissions = {
        "sofia": 0.12,
        "varna": 0.13,
        "plovdiv": 0.145
    }

if not town in commissions:
    has_errors = True

if has_errors:
    print("error")
else:
    commission_percent = commissions[town]
    earned = commission_percent * sales
    print("{0:.2f}".format(earned))
