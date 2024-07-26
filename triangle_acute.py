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

if first_side_length > second_side_length and first_side_length > third_side_length:
    c = first_side_length
    b = second_side_length
    a = third_side_length
elif second_side_length > first_side_length and second_side_length > third_side_length:
    c = second_side_length
    b = first_side_length
    a = third_side_length
else:
    c = third_side_length
    b = second_side_length
    a = first_side_length


if a**2 + b**2 == c**2:
    print("This Triangle is Right  Angled")
if a**2 + b**2 > c**2:
    print("This Triangle is acute")
else:
    print("This Triangle is obtuse")