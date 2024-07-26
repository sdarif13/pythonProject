first_number = int(input("Enter First Number:"))
second_number = int(input("Enter Second Number:"))
select_operand = input("Enter your operand:")

if select_operand == "+":
    sum = first_number + second_number
    print("Sum is", sum)
elif select_operand == "-":
    subtraction = first_number - second_number
    print("Subtraction is", subtraction)
elif select_operand == "*":
    multiplication = first_number * second_number
    print("Multiplication is", multiplication)
elif select_operand == "/":
    division = first_number / second_number
    print("Division is", division)
else:
    print("Enter Correct Input")
