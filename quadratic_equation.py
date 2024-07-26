import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

rules = b ** 2 - 4 * a * c

if rules > 0:
    sqrt_discriminant = math.sqrt(rules)
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
#    print(root1, root2)
    if root1 == root2:
        print("This Equation is Real and Equal.")
    else:
        print("This Equation is Real and Distinct.")
else:
    print("This Equation is Complex.")
