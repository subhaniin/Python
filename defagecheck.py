def is_major(age):
    return (
        "Allowed: Please carry your ID as age proof."
        if age >= 18
        else "Not allowed: Minors are not permitted."
    )

while True:
    user_input = input("Enter your age (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    try:
        age=int(user_input)
        if age<0:
            print("Age cannot be negative. Please enter a valid age.")
        elif age>125:
            print("age seems to be incorrect. Please enter a valid age.")
        else:
            print(is_major(age))
    except ValueError:
        print("Invalid input. Please enter a numeric age.")