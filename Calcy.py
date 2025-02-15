def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def modulus(x, y): return x % y
def exponentiate(x, y): return x ** y
def floor_divide(x, y): return "Error! Division by zero." if y == 0 else x // y

def get_number(prompt):
    """Get a valid float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculator():
    history = []
    prev_result = None

    while True:
        print("\n🔢 Simple Calculator")
        print("Operations: +  -  *  /  %  **  //")
        print("Enter 'history' to view past results or 'exit' to quit.")

        if prev_result is not None:
            print(f"🔹 Previous result: {prev_result}")

        num1_input = input("Enter the first number (or 'prev' for last result): ").strip()
        if num1_input.lower() == "exit":
            break
        elif num1_input.lower() == "history":
            print("\n📜 Calculation History:")
            for record in history:
                print(record)
            continue
        elif num1_input.lower() == "prev":
            if prev_result is None:
                print("No previous result available.")
                continue
            num1 = prev_result
        else:
            try:
                num1 = float(num1_input)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
                continue

        num2 = get_number("Enter the second number: ")
        operator = input("Enter the operator: ").strip()

        operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
            "%": modulus,
            "**": exponentiate,
            "//": floor_divide
        }

        if operator in operations:
            result = operations[operator](num1, num2)
            print(f"✅ Result: {result:.2f}" if isinstance(result, float) else f"✅ Result: {result}")
            history.append(f"{num1} {operator} {num2} = {result}")
            prev_result = result
        else:
            print("❌ Invalid operator. Please use a valid one.")

        # Exit condition
        if input("\nDo you want to continue? (yes/no): ").strip().lower() != "yes":
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    calculator()