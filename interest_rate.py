principal_amount = int(input("Enter Principal Amount: "))
interest_rate = int(input("Enter Interest Rate: "))
loan_year = int(input("Enter Loan Year: "))
certain_amount = int(input("Enter Certain Amount: "))

if principal_amount > 0:
    if interest_rate > 0:
        if loan_year > 0:
            interest = (principal_amount * interest_rate * loan_year) / 100
            print("Total Interest is:", interest)
            if interest > certain_amount:
                print("Interest is Above of Certain Amount.")
            else:
                print("Interest is Below of Certain Amount.")
        else:
            print("Invalid Loan Year.")
    else:
        print("Invalid Interest Rate.")
else:
    print("Invalid Principal Amount.")
