def area_perimeter(question, error):
    while True:
        response = input(question).lower()

        for item in calc_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


calc_list = ["area", "perimeter", "both"]

ask_question = area_perimeter("What do you need? ")
