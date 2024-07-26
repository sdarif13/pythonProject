first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))

if first_number == second_number:
    print("The numbers are Equal")
elif first_number != second_number:
    if first_number > second_number:
        print("Number is Not Equal. The First numbers is Bigger then Second Number")
    elif first_number < second_number:
        print("Number is Not Equal. The First numbers is Smaller then Second Number")
