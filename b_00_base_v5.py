import math
import pandas
import datetime


# Functions go here...

# Number checker function - Can specify numbers or whole integers depending on scenario...
def number_checker(question, error, input_type):
    while True:
        response = input(question)

        # Checks for exit code / blank space for <INFINITE>
        if response == "xxx" or response == "":
            return response

        # When the user inputs a number or integer / a valid input
        elif response != "":
            try:
                response = input_type(response)

                if response <= 0:
                    print(error)
                    continue

                else:
                    return response

            # Detects for value errors, displays error rather than crashing
            except ValueError:
                print(error)
                continue

        return response


# Checks what shape the user responds with...
def shape(question, error):
    while True:
        response = input(question).lower()

        for item in shape_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


# Checks user inputs to y / n questions...
def yes_no(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (yes / no)\n")


# Following functions are the calculations for the shapes / returning the calculations...
def circle(radius):
    area = round(math.pi * radius ** 2, 2)
    circumference = round(2 * math.pi * radius, 2)
    return f"The area is: {area} | The circumference is  {circumference}"


def square(side):
    area = round(side ** 2, 2)
    perimeter = round(4 * side, 2)
    return f"The area is: {area} | The perimeter is  {perimeter}"


def rectangle(length, width):
    area = round(length * width, 2)
    perimeter = round(2 * length + 2 * width, 2)
    return f"The area is: {area} | The perimeter is  {perimeter}"


# Responds to either Heron's-law-using triangle or base x height triangles...
def triangle(know_sides, side_a=None, side_b=None, side_c=None, base=None, height=None):

    if know_sides:

        if not side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b:
            return "This triangle is not valid (refer to Impossible Triangle Theorem)"

        s = (side_a + side_b + side_c) / 2
        area = round(math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c)), 2)
        perimeter = round(side_a + side_b + side_c, 2)
        return f"The area is: {area} | The perimeter is {perimeter}"

    else:
        area = 0.5 * base * height
        perimeter = "Unknown - cannot be calculated with given measurements..."
        return f"The area is: {area} | The perimeter is: {perimeter}"


# Main routine

# Lists for all valid inputs / responses...
shape_list = ["circle", "triangle", "square", "rectangle", "xxx"]
yesno_list = ["yes", "no", "xxx"]
calc_list = ["area", "perimeter", "both", "xxx"]

# Title...
print("==== AREA / PERIMETER Calculator ====\n")


# Main routine goes here...

# Checks to see if user has used program before, displays instructions,
# Loops if user inputs the exit_code trying to quit prematurely...
while True:
    display_instructions = yes_no("Have you used this tool before? ")

    if display_instructions == "xxx":
        print("Please use the calculator at least once!\n")
        continue

    elif display_instructions == "no":
        print("\n### Instructions ###\n"
              "This program allows the user to calculate the perimeter and area of simple shapes.\n"
              "First, input the number of questions you need help with, or <ENTER> if you don't know how many, then\n"
              "simply input the dimensions of the shape(s) and the perimeter, area, or even both will be calculated.\n"
              "At the end, a summary will be given of all the shapes, along with the calculations.\n")
        break

    else:
        print("Enjoy the tool's aide!\n")
        break

# Variable place holder
questions_answered = 0

# Asks how many questions user needs help with, accepts whole integers between 0 > x > 25,
# If user inputs "xxx" - same response and reason as above, <INFINITE MODE> is used if <ENTER> or > 25...
while True:
    questions_amount = number_checker("How many questions do you have, <ENTER> if you don't know and it will go until "
                                      "stopped: ", "Please enter a valid integer (more than 0)\n",
                                      int)

    if questions_amount == "xxx":
        print("Use this tool at least ONCE\n")
        continue

    elif questions_amount == "":
        break

    elif questions_amount >= 25:
        print("<INFINITE MODE> will be used instead.")
        break

    else:
        break

# Looping to mechanics, ends when user wants too, or if all questions have been helped..
end_tool = "no"
while end_tool != "yes":
    questions_answered += 1

    # Sets heading, changing per question
    if questions_amount == "" or questions_amount >= 25:
        heading = f"\nQuestion {questions_answered} of INFINITE Mode:"
    else:
        heading = f"\nQuestion {questions_answered} of {questions_amount}:"

    print(heading)

    # Ask user what shape they need help with, can quit if the user uses exit code
    ask_shape = shape("What shape do you need help with? ", "[Please enter 'circle', "
                                                            "'triangle', 'square', 'rectangle']")

    if ask_shape == "xxx":
        break

    # Prints what shape they have decided - makes it clear to user
    print(f"\nYou chose {ask_shape}.\n")

    if ask_shape == "circle":
        radius = number_checker("What is the radius? ", "Not valid", float)

        if radius == "xxx":
            break

        print(f"You said the radius is {radius}")
        answers = circle(radius)

    elif ask_shape == "triangle":
        ask_user = yes_no("Do you know all three sides (y / n)? ")

        if ask_user == "yes":
            side_a = number_checker("What is the length of side a? ", "Not valid", float)
            side_b = number_checker("What is the length of side b? ", "Not valid", float)
            side_c = number_checker("What is the length of side c? ", "Not valid", float)

            if side_a or side_b or side_c == "xxx":
                break

            answers = triangle(know_sides=True, side_a=side_a, side_b=side_b, side_c=side_c)

        elif ask_user == "no":
            base = number_checker("What is the base of the triangle? ", "Not valid", float)
            height = number_checker("What is the height of the triangle? ", "Not valid", float)

            if base or height == "xxx":
                break

            answers = triangle(know_sides=False, base=base, height=height)

        else:
            answers = "Invalid input. Could not calculate the area or perimeter."

    elif ask_shape == "square":
        side = number_checker("What is the length of any side? ", "Not valid", float)

        if side == "xxx":
            break

        print(f"You said the side length is {side}")
        answers = square(side)
    else:
        length = number_checker("What is the length of the rectangle? ", "Not valid", float)
        width = number_checker("What is the width of the rectangle? ", "Not valid", float)

        if length or width == "xxx":
            break

        print(f"You said the length was {length}, and width was {width}")
        answers = rectangle(length, width)

    print(answers)

    if questions_amount and questions_answered >= questions_amount:
        break
