def divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

def exponent(num1, num2):
    return num1 ** num2

def remainder(num1, num2):
    if num2 == 0:
        return None
    return num1 % num2

def summation(start, end):
    if start > end:
        return None
    return sum(range(start, end +1))

def main():
    while True:
        print("\nMathematical Operations menu")
        print("[D]. Division")
        print("[E]. Exponentiation")
        print("[R]. Remainder")
        print("[F]. Summation")
        print("[Q]. Exit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == 'Q':
            print("Exiting program...")
            break
        
        try:
            if choice == 'D':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = divide(num1, num2)
                if result is None:
                    print("Error: Cannot divide by zero!")
                else:
                    print(f"Result: {result}")

            elif choice == 'E':
                base = float(input("Enter base number: "))
                power = float(input("Enter power: "))
                result = exponent(base, power)
                print(f"Result: {result}")

            elif choice == 'R':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = remainder(num1, num2)
                if result is None:
                    print("Error: Cannot find remainder with zero!")
                else:
                    print(f"Result: {result}")

            elif choice == 'F':
                start = int(input("Enter start number: "))
                end = int(input("Enter end number: "))
                result = summation(start, end)
                if result is None:
                    print("Error: End number must be greater than start number!")
                else:
                    print(f"Result: {result}")

            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    main()