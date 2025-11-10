while True:
    s = input("Enter a number (or 'q' to quit): ")
    if s.lower() == 'q':
        break
    try:
        n = int(s)
        print("Cumulative sums from 1 to", n, ":")
        # We'll show cumulative sums up to a reasonable number
        if n <= 100:  # small numbers, show all
            for i in range(1, n+1):
                print(i*(i+1)//2, end=' ')
            print()
        else:  # for large numbers, show first 10 and last 10
            print("First 10:", end='  ')
            for i in range(1, 11):
                print(i*(i+1)//2, end='  ')
            print("... Last 10:", end='  ')
            for i in range(n-9, n+1):
                print(i*(i+1)//2, end='  ')
            print()
    except ValueError:
        print("Invalid input. Please enter an integer.")
