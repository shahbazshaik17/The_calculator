from art import logo
print(logo)
# the functions 
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    play = False
    while not play:

        num1 = float(input("enter the first number: "))
        for symbol in operations:
            print(symbol)
        chosen_op = input("pick an operation from the line above: ")
        num2 = float(input("enter the second number: "))
        
        if chosen_op in operations:
            calculation = operations[chosen_op]
            first_answer = calculation(num1, num2)
            print(f"{num1} {chosen_op} {num2} is {first_answer}")


            game_on  = input("play again press 'y' else 'n': ")
            if game_on == "y":
                play = False
            else:
                break
calculator()