temp_data_celsius = int(input("Enter Temperature in Celsius: "))
temp_data_fahrenheit = int(input("Enter Temperature in Fahrenheit: "))

celsius_to_fahrenheit = (temp_data_celsius * (9 / 5)) + 32
print(celsius_to_fahrenheit)

fahrenheit_to_celsius = (temp_data_fahrenheit - 32) / (9 / 5)
print(fahrenheit_to_celsius)

compare_data = (fahrenheit_to_celsius * (9 / 5)) + 32
print(compare_data)