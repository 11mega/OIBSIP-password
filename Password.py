import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_var.get()

    try:
        length = int(length)
        if length <= 0:
            raise ValueError
    except:
        messagebox.showerror("Invalid Input", "Password length must be a positive integer!")
        return

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


# ---------------- GUI ------------------

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x350")
root.config(bg="lightblue")

# Variables
length_var = tk.StringVar()
password_var = tk.StringVar()
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

# Widgets
tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)

tk.Label(root, text="Password Length:", font=("Arial", 12), bg="lightblue").pack()
tk.Entry(root, textvariable=length_var, width=10).pack()

tk.Label(root, text="Select Character Types:", font=("Arial", 12), bg="lightblue").pack(pady=10)

tk.Checkbutton(root, text="Letters", variable=letters_var, bg="lightblue").pack()
tk.Checkbutton(root, text="Numbers", variable=numbers_var, bg="lightblue").pack()
tk.Checkbutton(root, text="Symbols", variable=symbols_var, bg="lightblue").pack()

tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=10)

tk.Entry(root, textvariable=password_var, width=30, font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="black", fg="white").pack()

root.mainloop()
