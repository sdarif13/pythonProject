initial_amount = int(input("Enter Initial Amount: "))
deposit_amount = int(input("Enter Your Deposit Amount: "))
withdrawal_amount = int(input("Enter Your Withdrawals Amount: "))

if initial_amount >= 0:
    if deposit_amount >= 0:
        initial_amount = initial_amount + deposit_amount
        if withdrawal_amount >= 1:
            if withdrawal_amount <= initial_amount:
                initial_amount = initial_amount - withdrawal_amount
                print("Your Balance is: ", initial_amount)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Withdrawal Amount. Please Enter Valid Amount. Your Balance is: ", initial_amount)
    else:
        print("Invalid Deposit Amount. Please Enter Valid Amount. Your Balance is: ", initial_amount)
else:
    print("Invalid Initial Amount. Please Enter Valid Amount.")
