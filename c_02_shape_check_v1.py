def shape(question, error):
    while True:
        response = input(question).lower()

        for item in shape_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


shape_list = ["circle", "triangle", "square", "rectangle"]

# Loop for testing purposes
while True:
    ask_shape = shape("What shape? ", "Please enter a valid shape")

    if ask_shape == "circle":
        mode = "circle"

    elif ask_shape == "triangle":
        mode = "triangle"

    elif ask_shape == "square":
        mode = "square"

    else:
        mode = "rectangle"

    print(f"You've selected the {ask_shape}.")
    print()
