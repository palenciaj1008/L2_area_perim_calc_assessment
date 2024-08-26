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


def triangle(know_sides=True, side_a=True, side_b=True, side_c=True, base=True, height=True):

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


# Main component goes here...
shape_list = ["square", "triangle", "circle", "rectangle"]
yesno_list = ["yes", "no"]

ask_user = yes_no("Do you know all three sides (y / n)? ")
print()

if ask_user == "yes":
    side_a = number_checker("What is the length of side a? ", "Not valid", float)
    side_b = number_checker("What is the length of side b? ", "Not valid", float)
    side_c = number_checker("What is the length of side c? ", "Not valid", float)
    answers = triangle(know_sides=True, side_a=True, side_b=True, side_c=True, base=False, height=False)

elif ask_user == "no":
    base = number_checker("What is the base of the triangle? ", "Not valid", float)
    height = number_checker("What is the height of the triangle? ", "Not valid", float)
    answers = triangle(know_sides=False, side_a=False, side_b=False, side_c=False, base=True, height=True)

else:
    answers = "Invalid input. Could not calculate the area or perimeter."

print("\n*** RESULTS ***")
print(answers)
