import time
import os

colors = ["31", "32", "33", "34", "35", "36"]  # ANSI color codes

# Loop forever (Ctrl + C to stop)
while True:
    for n in range(1, 15):
        os.system("cls")  # use "clear" for Mac/Linux
        c = 0
        
        # Upper part
        for i in range(1, n + 1):
            print(f"\033[{colors[c]}m" + " " * (n - i) + " *" * i)
            c = (c + 1) % len(colors)

        # Lower part
        for i in range(n - 1, 0, -1):
            print(f"\033[{colors[c]}m" + " " * (n - i) + " *" * i)
            c = (c + 1) % len(colors)

        print("\033[0m")  # reset color
        time.sleep(0.1)  # ANIMATION SPEED