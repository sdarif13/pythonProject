first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
third_number = int(input("Enter Third Number: "))

if first_number > second_number and first_number > third_number:
    print("The Bigger Number is: ", first_number)
elif second_number > first_number and second_number > third_number:
    print("The Bigger Number is: ", second_number)
else:
    print("The Bigger Number is: ", third_number)

if first_number < second_number and first_number < third_number:
    print("The Smallest Number is: ", first_number)
elif second_number < first_number and second_number < third_number:
    print("The Smallest Number is: ", second_number)
else:
    print("The Smallest Number is: ", third_number)
