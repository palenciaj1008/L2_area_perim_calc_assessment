# Integer checker, used for components consisting of checking integers
# Code taken from "fundraising_calculator: number_checker_v2"
def number_checker(question, error, input_type):
    while True:
        response = input(question)

        if response.lower() == "xxx":
            print("Please use the tool at least ONCE\n")
            continue

        elif response == "":
            return response

        else:
            try:
                response = input_type(response)
                if response <= 0:
                    print(error)
                    continue

                return response

            except ValueError:
                print(error)
