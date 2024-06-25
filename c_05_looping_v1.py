def int_checker(question):

    while True:
        response = input(question)

        error = "Please enter a valid integer greater than 0"

        if response == "xxx":
            return response

        elif response != "":
            try:
                response = int(response)

                if response < 1:
                    print(error)
                    continue

            except ValueError:
                print(error)
                continue

        return response


# Rounds mechanics
questions_answered = 0

questions = int_checker("How many questions do you have? ")

# rounds loop
end_game = "no"
while questions != "xxx":

    heading = f"Question {questions_answered + 1} of {questions}"

    print(heading)
    choose = input(f"Enter a number or 'xxx' to end: ")
    questions_answered += 1

    if questions_answered == questions:
        break

    elif choose == "xxx":
        break

print("Thank you for using")
