def temperature_converter():
    conversion_type = input("Enter conversion type ('C2F' for Celsius to Fahrenheit, 'F2C' for Fahrenheit to Celsius, 'M2F' for Meter to Feet, 'F2M' for Feet to Meter): ")
    value = float(input("Enter the temperature or the distance value: "))

    if conversion_type == 'C2F':
        result = (value * 9/5) + 32
        print(value, "°C =", round(result, 2), "°F")

    if conversion_type == 'F2C':
        result = (value - 32) * 5/9
        print(value, "°F =", round(result, 2), "°C")
    
    if conversion_type == 'M2F':
        result = (3 * value)
        print(value, "M =", round(result, 2), "F")
        
    elif conversion_type == 'F2M':
        result = value/3
        print(value, "F =", round(result, 2), "M")
        
    else:
        print("Invalid input! Please enter 'C2F' or 'F2C'.")

temperature_converter()
