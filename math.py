try:
    a = float(input("Enter first no: "))
    b = float(input("Enter second no: "))
    
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")

except ValueError:
    print("Please enter valid numbers.")
