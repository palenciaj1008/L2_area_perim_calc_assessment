# Functions go here...
def instructions():

    print("Instructions go here")


def yes_no(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (yes / no)\n")


# Main routine goes here...
yesno_list = ["yes", "no"]

display_instructions = yes_no("Have you used this tool before? ")


# Displays instructions of user says 'yes', loop breaks and continues with rest of code
if display_instructions == "no":
    print(display_instructions)
    print(instructions)

print("\nprogram continues")
