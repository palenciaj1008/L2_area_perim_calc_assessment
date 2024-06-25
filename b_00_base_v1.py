# Imports go here...
import math
import pandas


# Functions go here...

def number_checker(question, error, input_type):

    while True:
        try:
            response = input_type(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


def shape(question, error):
    while True:
        response = input(question).lower()

        for item in shape_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


def yes_no(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (yes / no)\n")


def area_perimeter(question, error):
    while True:
        response = input(question).lower()

        for item in calc_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


# Main routine goes here...

# Lists go here...
shape_list = ["circle", "triangle", "square", "rectangle", "xxx"]
yesno_list = ["yes", "no", "xxx"]
calc_list = ["area", "perimeter", "both", "xxx"]
