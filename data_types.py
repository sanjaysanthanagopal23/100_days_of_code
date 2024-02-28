# script to understand python data types in chapter 2
# Data types :
# 1. strings, integers, float and boolean
# a. strings :
# subscript / indexing

# sample = "Hello"
# print(sample[4])

# print("123" + "456")  # string concatenation
# type casting
# most readable code :

def sum_of_char(input_string):

    first_digit = int(input_string[0])
    second_digit = int(input_string[1])

    print(first_digit + second_digit)

    return None


# sum_of_char("45")

# Mathematical operator
# ** - exponent

# print((3 * (3 + 3) / 3 - 3))

def calculate_bmi(height: int, weight: int) -> int:

    """
    :param height: represents the height of the individual whose BMI has to be calculated
    :param weight: represents the weight of the individual whose BMI has to be calculated
    :return: Body max index value of the individual
    """

    bmi = weight / (height ** 2)

    return bmi


# bmi = calculate_bmi(height=1.82, weight=67)
# print("your bmi ==>", bmi)

# floor division // will return an int as output instead of a float !
# +=, -=, *=, /=

# F string : easy for printing :

# score = 1
# height = 1.8
#
# print(f"your score is {score} and height is {height}")


def life_in_weeks(current_age: int) -> int:

    """
    :param current_age: An integer that represents the current age of the user
    :return: An integer that represents the remaining life in weeks for the user
    """

    total_age_in_weeks = 4000
    num_of_weeks_in_a_year = 52

    age_in_weeks = int(current_age) * num_of_weeks_in_a_year
    remaining_life = total_age_in_weeks - age_in_weeks

    print(f"You have {remaining_life} weeks left.")

    return remaining_life


# rul = life_in_weeks(current_age=36)


def bill_calculator(total_bill: float, tip_percentage: int, num_of_guests: int) -> float:

    """
    :param total_bill: total bill that needs to be paid to the restaurant
    :param tip_percentage: % of tips that the guests are willing to give
    :param num_of_guests: total number of guests
    :return: share of each person
    """

    print("Welcome to bill calculator !")
    individual_share = (total_bill + (total_bill * (tip_percentage / 100))) / num_of_guests
    final = "{:.2f}".format(individual_share)
    print(f"Each person should pay: ${final}")

    return final


split = bill_calculator(total_bill=4550.50, tip_percentage=12, num_of_guests=7)
