first_side_length = int(input("Enter First Side Length: "))
second_side_length = int(input("Enter Second Side Length: "))
third_side_length = int(input("Enter Third Side Length: "))

if first_side_length >= second_side_length and first_side_length >= third_side_length:
    if (second_side_length + third_side_length) > first_side_length:
        print("It is a Valid Triangle")
    else:
        print("It is not a Valid Triangle")
elif second_side_length > first_side_length and second_side_length > third_side_length:
    if (first_side_length + third_side_length) > second_side_length:
        print("It is a Valid Triangle")
    else:
        print("It is not a Valid Triangle")
elif third_side_length > first_side_length and third_side_length > second_side_length:
    if (first_side_length + second_side_length) > third_side_length:
        print("It is a Valid Triangle")
    else:
        print("It is not a Valid Triangle")
else:
    print("It is not a Valid Triangle")

if first_side_length == second_side_length or first_side_length == third_side_length or second_side_length == third_side_length:
    if first_side_length == second_side_length == third_side_length:
        print("This Triangle is a equilateral.")
    else:
        print("This Triangle is a isosceles.")
else:
    print("This Triangle is a scalene.")
