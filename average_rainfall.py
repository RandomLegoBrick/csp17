#
# Matthew Anderson 3/30/2025
#

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# generic function to validate input for either floats (rainfall) or integers (year span)

# credit to this post for how to handle errors when trying to convert non numeric data to an int or float
# https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python

def validate_int(message, greater_than_equal=None, request_float=False):
    while True:
        try:
            # request either an integer or a float from the user
            if request_float:
                user_input = float(input(message))
            else:
                user_input = int(input(message))

            if (greater_than_equal == None) or (greater_than_equal != None and user_input >= greater_than_equal):
                return user_input
            elif (greater_than_equal != None and user_input < greater_than_equal):

                # if the number is less than the required amount, notify the user
                print(f"Invalid input, must be greater than or equal to {greater_than_equal}")

        except ValueError:

            # in the case of non numeric data, ask the user to retry
            print("Invalid input, please enter a number.")


def getYears():
    return validate_int("Enter a number of years: ", 0)

def getMonthlyRain(month):
    return validate_int(f"Rainfall during {month} (in): ", 0, True)

def calcAvgRain(period_of_years):

    total_rainfall = 0
    number_of_months = period_of_years * 12

    # loop through the number of years
    for year in range(1, period_of_years+1):
        print(f"\n-- Year {year} -- ")

        # find rain for each month
        for month in MONTHS:
            total_rainfall += getMonthlyRain(month)

    average_monthly_rainfall = total_rainfall / number_of_months

    # Output nessasary data
    print(f"\n-- Rainfall Over {period_of_years} Year{'s' if period_of_years > 1 else ''} --")
    print(f"Data gathered for a {number_of_months} month period.")
    print(f"Total rainfall was {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall was {average_monthly_rainfall:.2f} inches")


if __name__ == "__main__":

    # Welcome message
    print("-- Average Rainfall Calculator --")
    print("Find the average rainfall in inches over a specific span of years")
    print()

    period_of_years = getYears()

    calcAvgRain(period_of_years)