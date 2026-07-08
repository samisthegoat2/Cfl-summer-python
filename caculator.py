# Simple calculator that performs all operations without asking for choice

def calculate_all(a, b):
    """Perform addition, subtraction, multiplication, and division."""
    results = {}

    # Addition
    results['addition'] = a + b

    # Subtraction
    results['subtraction'] = a - b

    # Multiplication
    results['multiplication'] = a * b

    # Division with zero check
    if b != 0:
        results['division'] = a / b
    else:
        results['division'] = "Undefined (division by zero)"

    return results


def main():
    try:
        # Get user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform all operations
        results = calculate_all(num1, num2)

        # Display results
        print("\nResults:")
        for operation, value in results.items():
            print(f"{operation.capitalize()}: {value}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()