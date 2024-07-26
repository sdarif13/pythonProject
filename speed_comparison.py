speed_kph = float(input("Enter speed in km/h: "))
speed_mph = float(input("Enter speed in mph: "))

if speed_kph == speed_mph:
    mph_to_kph = speed_mph * 1.60934
    if speed_kph < mph_to_kph:
        print("Miles is Faster then Kilometer.")
    elif speed_kph > mph_to_kph:
        print("Kilometer is Faster then Miles.")
    else:
        print("Both speeds are equal.")
else:
    print("Enter Same Value for Comparison.")
