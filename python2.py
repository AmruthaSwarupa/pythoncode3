year = 2015
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("You entered year is a leap year.")
        else:
            print("You entered year is not a leap year.")
    else:
        print("You entered year is a leap year.")
else:
    print("You entered year is not a leap year.")