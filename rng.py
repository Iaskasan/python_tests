import tkinter as tk
import random

def generate_random_number():
    try:
        a = int(lower_bound_entry.get())
        b = int(upper_bound_entry.get())
        if a > b:
            a, b = b, a
        result = random.randint(a, b)
        result_label.config(text=f"Random Number: {result}")
    except ValueError:
        result_label.config(text="Please enter valid integers.")

app = tk.Tk()
app.title("Random Number Generator")

tk.Label(app, text="Enter Lower Bound (a):").pack()
lower_bound_entry = tk.Entry(app)
lower_bound_entry.pack()

tk.Label(app, text="Enter Upper Bound (b):").pack()
upper_bound_entry = tk.Entry(app)
upper_bound_entry.pack()

generate_button = tk.Button(app, text="Generate", command=generate_random_number)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
