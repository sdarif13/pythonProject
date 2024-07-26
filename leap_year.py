year = int(input("Enter A Year: "))

result = year % 4

if year > 1582:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "Year is Leap Year")
    else:
        print(year, "Year is not Leap Year")
else:
    print("Year must be greater than 1582. Please Enter Correct Year.")
