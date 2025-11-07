birth_year = int(input("Enter your birth year: "))
age = 2025 - birth_year

if age >= 0 and age <= 12:
    print(f"Your age is {age}, and you are a child.")
elif age >= 13 and age <= 17:
    print(f"Your age is {age}, and you are a teenager.")
elif age >= 18 and age <= 64:
    print(f"Your age is {age}, and you are an adult.")
elif age >= 65:
    print(f"Your age is {age}, and you are a senior.")
else:
    print("Invalid age entered.")
