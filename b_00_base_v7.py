import math
import pandas
from datetime import date


# Functions go here...

# Number checker function - Can specify numbers or whole integers depending on scenario...
def number_checker(question, error, input_type, allow_blank=False):
    while True:
        response = input(question)

        # If blank input is allowed, return the blank response
        if allow_blank and response == "":
            return response

        # Checks for exit code / blank space for <INFINITE>
        if response == "xxx":
            return response

        # Prevent blank input when measurements are being asked
        elif response == "":
            print(error)
            continue

        # When the user inputs a number or integer / a valid input
        else:
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


# Checks the users input - depends on the list, outputs appropriate responses, and / or errors...
def user_input(question, error, valid_list):
    while True:
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


# Following functions are the calculations for the shapes / returning the calculations...
def circle(circle_radius):
    area = round(math.pi * circle_radius ** 2, 2)
    circumference = round(2 * math.pi * circle_radius, 2)
    return f"AREA: {area} U^2 | CIRCUMFERENCE: {circumference} U"


def square(square_side):
    area = round(square_side ** 2, 2)
    perimeter = round(4 * square_side, 2)
    return f"AREA: {area} U^2 | PERIMETER: {perimeter} U"


def rectangle(rec_length, rec_width):
    area = round(rec_length * rec_width, 2)
    perimeter = round(2 * (rec_length + rec_width), 2)
    return f"AREA: {area} U^2 | PERIMETER: {perimeter} U"


# Responds to either Heron's-law-using triangle or base x height triangles...
def triangle(know_sides, tri_side_a=None, tri_side_b=None, tri_side_c=None, tri_base=None, tri_height=None):

    if know_sides:

        if (not tri_side_a + tri_side_b > tri_side_c and tri_side_b + tri_side_c >
                tri_side_a and tri_side_a + tri_side_c > tri_side_b):
            return "This is an 'Invalid Triangle'"

        s = (tri_side_a + tri_side_b + tri_side_c) / 2
        area = round(math.sqrt(s * (s - tri_side_a) * (s - tri_side_b) * (s - tri_side_c)), 2)
        perimeter = round(tri_side_a + tri_side_b + tri_side_c, 2)
        return f"AREA: {area} U^2 | PERIMETER: {perimeter} U"

    else:
        area = 0.5 * tri_base * tri_height
        return f"AREA: {area} U^2 | PERIMETER: {"N / A"}"


# Main routine...
# Lists for all valid inputs / responses...
shape_list = ["circle", "triangle", "square", "rectangle", "xxx"]
yesno_list = ["yes", "no", "xxx"]

# Dictionaries and lists - for pandas / dataframe
shapes_selected_list = []
answers_list = []

calculations_list = {
    "Shape": shapes_selected_list,
    "Answer": answers_list
}

# Title...
print("==== AREA / PERIMETER Calculator ====\n")


# Main routine goes here...

# Variable placeholders, prevents NameErrors, and unresolved references
answers = ""
questions_answered = 0

# Checks to see if user has used program before, displays instructions,
# Loops if user inputs the exit_code trying to quit prematurely...
while True:
    display_instructions = user_input("Have you used this tool before? ",
                                      "Please input 'y' / 'n'", yesno_list)

    if display_instructions == "xxx":
        print("Please use the calculator at least once!\n")
        continue

    elif display_instructions == "no":
        print("\n### Instructions ###\n"
              "This program allows the user to calculate the perimeter and area of simple shapes.\n"
              "First, input the number of questions you need help with, or <ENTER> if you don't know how many, then\n"
              "simply input the dimensions of the shape(s) and the perimeter, area, or even both will be calculated.\n"
              "At the end, a summary will be given of all the shapes, along with the calculations.\n\n"
              "Note - Possible shapes are: Circle, Triangle, Square, Rectangle\n"
              "     - U = Unit, used as a placeholder for you metric units\n"
              "     - Units will be rounded to two decimal points\n")
        break

    else:
        print("Enjoy the tool's aide!\n")
        break

# Asks how many questions user needs help with, accepts whole integers between 0 > x > 25,
# If user inputs "xxx" - same response and reason as above, <INFINITE MODE> is used if <ENTER> or > 25...
while True:
    questions_amount = number_checker("How many questions do you have, <ENTER> if you don't know and it will go until "
                                      "stopped: ", "Please enter a valid integer (more than 0)\n",
                                      int, allow_blank=True)

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

# Looping to mechanics, ends when user wants too, or if all questions have been helped...
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
    shape_select = user_input("What shape do you need help with ('xxx' to quit)? ",
                              "[Please enter 'circle', 'triangle', 'square', 'rectangle']", shape_list)

    if shape_select == "xxx":
        break

    # Prints what shape they have decided - makes it clear to user
    print(f"\n|----- You chose {shape_select} -----|\n")

    # Circle section, asks for radius - used in calculations, quits if "xxx"
    if shape_select == "circle":
        radius = number_checker("What is the radius? ", "Enter a valid number (> 0)", float,
                                allow_blank=False)

        if radius == "xxx":
            break

        # Prints the radius user said, sets the answer for printing in the end
        print(f"\n** You said the radius is: {radius} **\n")
        answers = circle(radius)

    # Triangle section, has two parts for heron's law, and base x height, quits if "xxx"
    elif shape_select == "triangle":
        ask_user = user_input("Do you know all three sides (y / n)? ",
                              "Please input 'y' / 'n'", yesno_list)

        # Ends program when exit code used
        if ask_user == "xxx":
            break

        # Heron's law works if user knows all 3 sides, gives area and perimeter
        elif ask_user == "yes":

            print("\n(---- Heron's Law Triangle ----)")

            side_a = number_checker("What is the length of side a? ", "Enter a valid number (> 0)",
                                    float, allow_blank=False)

            if side_a == "xxx":
                break

            side_b = number_checker("What is the length of side b? ", "Enter a valid number (> 0)", float,
                                    allow_blank=False)

            if side_b == "xxx":
                break

            side_c = number_checker("What is the length of side c? ", "Enter a valid number (> 0)",
                                    float, allow_blank=False)

            if side_c == "xxx":
                break

            # Tells user what they said the side values are, sets answer for printing
            print(f"\n** You said the sides are {side_a}, {side_b}, and {side_c} **\n")
            answers = triangle(know_sides=True, tri_side_a=side_a, tri_side_b=side_b, tri_side_c=side_c)

        # Base and height only give area, cannot give perimeter
        elif ask_user == "no":
            print("\n(---- Standard Triangle ----)")
            base = number_checker("What is the base of the triangle? ", "Enter a valid number (> 0)", float,
                                  allow_blank=False)

            if base == "xxx":
                break

            height = number_checker("What is the height of the triangle? ", "Enter a valid number (> 0)",
                                    float, allow_blank=False)

            if height == "xxx":
                break

            # Tells user what they said the base and height are, sets answer for printing
            print(f"\n** You said the base: {base}, and height: {height} **\n")
            answers = triangle(know_sides=False, tri_base=base, tri_height=height)

        # Controls whether program continues processing shapes, or not
        else:
            end_tool = "yes"

    # Square section, asks user for a side length, gives area and perimeter, "xxx" = quit
    elif shape_select == "square":
        side = number_checker("What is the length of any side? ", "Enter a valid number (> 0)", float,
                              allow_blank=False)

        if side == "xxx":
            break

        # Tells user what they said side value is, sets answer for printing
        print(f"\n** You said the side length is {side} **\n")
        answers = square(side)

    # Rectangle section, asks for the length and width, gives are and perimeter, "xxx" to quit
    else:
        length = number_checker("What is the length of the rectangle? ", "Enter a valid number (> 0)",
                                float, allow_blank=False)

        if length == "xxx":
            break

        width = number_checker("What is the width of the rectangle? ", "Enter a valid number (> 0)",
                               float, allow_blank=False)

        if width == "xxx":
            break

        # Tells user what they said length and width is, sets answer for printing
        print(f"\n** You said the length was {length}, and width was {width} **\n")
        answers = rectangle(length, width)

    # Prints the answer set from the shape sections
    print(answers)

    # Add shape(s) and answer(s) to lists
    shapes_selected_list.append(shape_select)
    answers_list.append(answers)

    # Once all questions has been answered, program ends
    if questions_answered == questions_amount:
        print("\nAll questions have been answered\n"
              "Displaying table...")
        break

# Printing Area...

print()

# Only generates a dataframe and file if the user has received measurements for at least ONE shape
if questions_answered >= 1 and shapes_selected_list and answers_list:

    # Get current date for heading and file name
    today = date.today()

    # Sets the heading for the file, sets title of the file
    print_heading = "<|==== AREA / PERIMETER Results ====|>"
    filename = f"{today.strftime("%d")}_{today.strftime("%m")}_{today.strftime("%y")} - Area_Perimeter_Tool"

    tool_frame = pandas.DataFrame(calculations_list)
    answers_txt = pandas.DataFrame.to_string(tool_frame)

    to_write = [print_heading, answers_txt]

    # Print Output
    for print_item in to_write:
        print(print_item)

    # Write output to file
    # Create file to hold data (add .txt extension)
    file_name = f"{filename}.txt"
    text_file = open(file_name, "w+")

    for print_item in to_write:
        text_file.write(print_item)
        text_file.write("\n")

    # Close the file
    text_file.close()

# If user does not input measurements for at least ONE shape, gives an output
else:
    print("Unable to display results - Lack of measurements")

# Thanks user for using program...
print("\nThank you for using this tool!")
n