import math


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


# Functions for calculating shape's area and perimeter...
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


def triangle(side_a, side_b, side_c):
    s = (side_a + side_b + side_c) / 2
    area = round(math.sqrt(s * (s-side_a) * (s - side_b) * (s - side_c)), 2)
    perimeter = round(side_a + side_b + side_c, 2)
    return f"The area is: {area} | The perimeter is  {perimeter}"


shape_list = ["square", "triangle", "circle", "rectangle"]
yesno_list = ["yes", "no"]

ask_shape = shape("What shape? ", "Not valid shape")

print(f"Shape selected: {ask_shape}\n")

if ask_shape == "circle":
    radius = number_checker("What is the radius? ", "Not valid", float)
    print(f"You said the radius is {radius}")
    answers = circle(radius)

elif ask_shape == "square":
    side = number_checker("What is the length of any side? ", "Not valid", float)
    print(f"You said the side length is {side}")
    answers = square(side)

elif ask_shape == "rectangle":
    length = number_checker("What is the length of the rectangle? ", "Not valid", float)
    width = number_checker("What is the width of the rectangle? ", "Not valid", float)
    answers = rectangle(length, width)

else:
    side_a = number_checker("What is the length of side a? ", "Not valid", float)
    side_b = number_checker("What is the length of side b? ", "Not valid", float)
    side_c = number_checker("What is the length of side c? ", "Not valid", float)
    answers = triangle(side_a, side_b, side_c)

print("\n*** RESULTS ***")
print(answers)
