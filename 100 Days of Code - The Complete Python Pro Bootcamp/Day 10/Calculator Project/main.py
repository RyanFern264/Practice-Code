from symbol import return_stmt


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calculator(chosen_operator,first_number, second_number):
    result = 0
    if chosen_operation == "+":
        result = operations[chosen_operation](first_number, second_number)
        print(f"{first_number} + {second_number} = {result}")
    if chosen_operation == "-":
        result = operations[chosen_operation](first_number, second_number)
        print(f"{first_number} - {second_number} = {result}")
    if chosen_operation == "*":
        result = operations[chosen_operation](first_number, second_number)
        print(f"{first_number} * {second_number} = {result}")
    if chosen_operation == "/":
        result = operations[chosen_operation](first_number, second_number)
        print(f"{first_number} / {second_number} = {result}")
    return result
operations = {"+":add, "-":subtract, "*":multiply, "/":divide}

print(operations["*"](4, 8))

calculating = True
while calculating:
    first_number = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    chosen_operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    result = calculator(chosen_operation, first_number, second_number)
    continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    while continue_calculation == "y":
        first_number = result
        print("+\n-\n*\n/")
        chosen_operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = calculator(chosen_operation, first_number, second_number)
        continue_calculation = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
