import datetime


def get_birthdate():
    while True:
        try:
            day = int(input('Enter the day you were born (1-31): '))
            month = int(input('Enter the month you were born (1-12): '))
            year = int(input('Enter the year you were born: '))

            birthdate = datetime.datetime(year, month, day)

            if birthdate <= datetime.datetime.now():
                return birthdate
            else:
                print("Invalid date. Please enter a valid birthdate.")
        except ValueError:
            print("Invalid input. Please enter valid numbers for day, month, and year.")


def calculate_age(birthdate):
    current_date = datetime.datetime.now()
    age = current_date - birthdate

    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    hours = age.seconds // 3600

    return years, months, days, hours


birthdate = get_birthdate()
years_lived, months_lived, days_lived, hours_lived = calculate_age(birthdate)

print("\nYou were born on:", birthdate.strftime("%B %d, %Y"))
print("You have lived for:")
print("Years:", years_lived)
print("Months:", months_lived)
print("Days:", days_lived)
print("Hours:", hours_lived)

current_date = datetime.datetime.now()
remaining_years = 100 - years_lived  # Assume a life expectancy of 100 years
remaining_months = (remaining_years * 365 * 30 - (years_lived * 365 * 30 + months_lived * 30)) // 30
remaining_days = (remaining_years * 365 - (years_lived * 365 + months_lived * 30 + days_lived))
remaining_hours = remaining_years * 365 * 24 - (years_lived * 365 * 24 + months_lived * 30 * 24 + days_lived * 24 +
                                                hours_lived)

print("\nAssuming a life expectancy of 100 years, you have:")
print("Remaining Years:", remaining_years)
print("Remaining Months:", remaining_months)
print("Remaining Days:", remaining_days)
print("Remaining Hours:", remaining_hours)
