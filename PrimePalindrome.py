def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def check_number(n):
    """Check if the number is prime, palindrome, or both."""
    prime = is_prime(n)
    palindrome = is_palindrome(n)
    
    if prime and palindrome:
        print(f"{n} is both Prime and Palindrome! 🚀")
    elif prime:
        print(f"{n} is a Prime number.")
    elif palindrome:
        print(f"{n} is a Palindrome number.")
    else:
        print(f"{n} is neither Prime nor Palindrome.")

# Loop until user exits
while True:
    user_input = input("\nEnter a number (or type 'exit' to quit): ").strip().lower()
    
    if user_input == "exit":
        print("Goodbye! 👋")
        break  # Exit the loop
    
    if user_input.isdigit():
        num = int(user_input)
        check_number(num)
    else:
        print("Invalid input! Please enter a valid number or type 'exit' to quit.")