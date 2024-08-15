import math


# Functions
def number_checker(question, error, input_type):
    while True:
        response = input(question)

        if response.lower() == "xxx":
            return response

        else:
            try:
                response = input_type(response)

                if response <= 0:
                    print(error)
                    continue

                else:
                    return response

            except ValueError:
                print(error)
                continue


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


# Main routine

# Lists
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
              "First, input the number of questions you need help with, or <ENTER> if you don't know how many, then\n"
              "simply input the dimensions of the shape(s) and the perimeter, area, or even both will be calculated.\n"
              "At the end, a summary will be given of all the shapes, along with the calculations.\n")
        break

    else:
        print("Enjoy the tool's aide!\n")
        break

# Variable place holder
questions_answered = 0

while True:
    questions_amount = input("How many questions do you have? (Press <ENTER> for infinite mode): ")

    if questions_amount.lower() == "xxx":
        print("Use this tool at least ONCE\n")
        continue

    elif questions_amount.isdigit() and int(questions_amount) >= 25:
        print("Please use <INFINITE> mode instead")
        continue

    elif questions_amount.isdigit():
        questions_amount = int(questions_amount)
        break

    else:
        questions_amount = ""  # Infinite mode
        break

end_tool = "no"
while end_tool != "yes":
    questions_answered += 1

    if questions_amount == "":
        heading = f"\nQuestion {questions_answered} of INFINITE Mode:"
    else:
        heading = f"\nQuestion {questions_answered} of {questions_amount}:"

    print(heading)

    ask_shape = shape("What shape do you need help with? ", "[Please enter 'circle', "
                                                            "'triangle', 'square', 'rectangle']")

    if ask_shape == "xxx":
        break

    print(f"\nYou chose {ask_shape}.\n")

    if ask_shape == "circle":
        radius = number_checker("What is the radius of the circle? ",
                                "Please enter a valid number (>0)", float)

        if radius == "xxx":
            break

        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        print(f"The area is: {area} | The circumference is  {circumference}")

    elif ask_shape == "triangle":
        side_a = number_checker("What is the length of side 'a'? ",
                                "Please enter a valid number (>0)", float)
        if side_a == "xxx":
            break

        side_b = number_checker("What is the length of side 'b'? ",
                                "Please enter a valid number (>0)", float)
        if side_b == "xxx":
            break

        side_c = number_checker("What is the length of side 'c'? ",
                                "Please enter a valid number (>0)", float)
        if side_c == "xxx":
            break

        s = (side_a + side_b + side_c) / 2
        area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
        perimeter = side_a + side_b + side_c
        print(f"The area is: {area} | The perimeter is  {perimeter}")

    elif ask_shape == "square":
        side = number_checker("What is the length of one side? ",
                              "Please enter a valid number (>0)", float)
        if side == "xxx":
            break

        area = side ** 2
        perimeter = 4 * side
        print(f"The area is: {area} | The perimeter is  {perimeter}")

    else:
        length = number_checker("What is the length? ",
                                "Please enter a valid number (>0)", float)
        if length == "xxx":
            break

        width = number_checker("What is the width? ",
                               "Please enter a valid number (>0)", float)
        if width == "xxx":
            break

        area = length * width
        perimeter = 2 * (length + width)
        print(f"The area is: {area} | The perimeter is  {perimeter}")

    if questions_amount and questions_answered >= questions_amount:
        break
