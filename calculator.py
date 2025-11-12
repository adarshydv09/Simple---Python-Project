"""
Simple Calculator - Performs basic arithmetic operations
Author: Your Name
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract second number from first"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide first number by second"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    """Raise first number to the power of second"""
    return a ** b

def modulus(a, b):
    """Get remainder of division"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a % b

def display_menu():
    """Show calculator menu"""
    print("\n=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Exit")
    print("=" * 25)

def get_numbers():
    """Get two numbers from user"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers")
        return None, None

def main():
    """Main calculator function"""
    print("Welcome to Simple Calculator!")
    
    while True:
        display_menu()
        choice = input("\nSelect operation (1-7): ")
        
        if choice == '7':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice! Please select 1-7.")
            continue
        
        num1, num2 = get_numbers()
        
        if num1 is None or num2 is None:
            continue
        
        # Perform calculation based on choice
        if choice == '1':
            result = add(num1, num2)
            print(f"\n{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"\n{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\n{num1} × {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"\n{num1} ÷ {num2} = {result}")
        elif choice == '5':
            result = power(num1, num2)
            print(f"\n{num1} ^ {num2} = {result}")
        elif choice == '6':
            result = modulus(num1, num2)
            print(f"\n{num1} % {num2} = {result}")

if __name__ == "__main__":
    main()