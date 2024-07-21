# Imports go here...
import math
import pandas


# Functions go here...
def number_checker(question, error, input_type):
    while True:
        response = input(question)

        if response.lower() == "xxx":
            print("Please use the tool at least ONCE\n")
            continue

        elif response == "":
            return response  # This will represent infinite mode

        else:
            try:
                response = input_type(response)
                if response <= 0:
                    print(error)
                    continue

                return response

            except ValueError:
                print(error)

# Usage in your main code


questions_amount = number_checker("How many questions do you have? <ENTER> for infinite mode: ",
                                  "Please enter a valid number greater than 0.\n", int)


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

print("==== AREA / PERIMETER Calculator ====\n")

while True:

    display_instructions = yes_no("Have you used this tool before? ")

    if display_instructions == "xxx":
        print("Please use the calculator at least once!\n")
        continue

    elif display_instructions == "no":
        print("\n### Instructions ###\n"
              "This program allows the user to calculate the perimeter and area of simple shapes.\n"
              "First, input the amount of questions you need help with, or <ENTER> if you don't know how many, then\n"
              "simply input the dimensions of the shape(s) and the perimeter, area, or even both will be calculated.\n"
              "At the end, a summary will be given of all the shapes, along with the calculations.\n")
        break

    else:
        print("Enjoy the ease of calculations!\n")
        break

questions_answered = 0

while True:
    questions_amount = number_checker("How many questions do you have, <ENTER> if you don't know and it will go until "
                                      "stopped: ", "Please enter a valid integer (more than 0)\n",
                                      int)

    if questions_amount == "xxx":
        print("Please use this tool ONCE\n")

    else:
        break

end_calculations = "no"
while end_calculations != "yes":
    questions_answered += 1

    if questions_amount == "":
        heading = f"\nQuestion {questions_answered} of INFINITE Mode:"

    else:
        heading = f"\nQuestion {questions_answered} of {questions_amount}:"

    print(heading)

    ask_shape = shape
    print()

# NOTE: ask user what shape they want, then ask for dimensions, then what they want to know
