body_fat = int(input("Enter Body Fat: "))
weight = int(input("Enter Body Weight: "))

body_fat_percentage = (body_fat / weight) * 100
print("Your Body Fat Percentage is", body_fat_percentage)

if body_fat_percentage < 8:
    print("Fat percentage is Very lean range")
elif 8 <= body_fat_percentage <= 19:
    print("Fat percentage is lean range")
elif 19 <= body_fat_percentage <= 25:
    print("Fat percentage is Healthy range")
elif 25 <= body_fat_percentage <= 32:
    print("Fat percentage is Average range")
elif body_fat_percentage > 32:
    print("Fat percentage is Overweight range")
