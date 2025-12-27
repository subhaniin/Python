import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Window
root = tk.Tk()
root.title("Digital Calculator")
root.geometry("300x400")

# Display
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", padx=10, pady=10)

# Buttons
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for btn in buttons:
    if btn == "=":
        tk.Button(frame, text=btn, width=10, height=3, command=calculate).grid(row=row, column=col, columnspan=2)
        col += 2
    else:
        tk.Button(frame, text=btn, width=5, height=3,
                  command=lambda b=btn: click(b)).grid(row=row, column=col)
        col += 1

    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="Clear", width=25, height=2, command=clear).pack(pady=5)

root.mainloop()
