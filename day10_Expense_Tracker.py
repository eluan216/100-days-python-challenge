import tkinter as tk
from tkinter import ttk, messagebox

expenses = []

window = tk.Tk()
window.title("Day 10 - Expense Tracker")
window.geometry("650x550")
window.configure(bg="#18212F")

title = tk.Label(window, text="Expense Tracker", font=("Arial", 24, "bold"), bg="#18212F", fg="#FFFFFF")
title.pack(pady=10)

total_label = tk.Label(window, text="Total Expenses: ₦0.00", font=("Arial", 16), bg="#18212F", fg="#FFFFFF")
total_label.pack(pady=10)

form = tk.Frame(window, bg="#18212F")
form.pack(pady=10)

tk.Label(form, text="Description:", font=("Arial", 12), bg="#18212F", fg="#FFFFFF").grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(form, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form, text="Amount (₦):", font=("Arial", 12), bg="#18212F", fg="#FFFFFF").grid(row=1, column=0, padx=5, pady=5)

amount_entry = tk.Entry(form, font=("Arial", 12))
amount_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form, text="Category:", font=("Arial", 12), bg="#18212F", fg="#FFFFFF").grid(row=2, column=0, padx=5, pady=5)

category_box = ttk.Combobox(form, font=("Arial", 12), values=["Food", "Transportation", "Entertainment", "Utilities", "Bills", "Education", "Health", "Shopping", "Other"], state="readonly")
category_box.grid(row=2, column=1, padx=5, pady=5)
category_box.set("Food")

columns = ("Name", "Amount", "Category")
table = ttk.Treeview(window, columns=columns, show="headings")

table.heading("Name", text="Expense")
table.heading("Amount", text="Amount (₦)")
table.heading("Category", text="Category")

table.column("Name", width=200)
table.column("Amount", width=150, anchor="center")
table.column("Category", width=150, anchor="center")

table.pack(padx=20, pady=10, fill="x")

def update_total():
    total = sum(expense["amount"] for expense in expenses)
    total_label.config(text=f"Total Expenses: ₦{total:.2f}")

def add_expense():
    name = name_entry.get().strip()
    amount_str = amount_entry.get().strip()
    category = category_box.get()

    if not name or not amount_str:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    try:
        amount = float(amount_str)

        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid positive number for the amount.")
        return

    expense = {"name": name, "amount": amount, "category": category}
    expenses.append(expense)

    table.insert("", "end", values=(name, f"₦{amount:.2f}", category))

    update_total()

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_box.set("Food")

def delete_expense():
    selected_item = table.selection()

    if not selected_item:
        messagebox.showerror("Selection Error", "Please select an expense to delete.")
        return

    for item in selected_item:
        values = table.item(item, "values")
        name, amount_str, category = values
        amount = float(amount_str.replace("₦", ""))

        expenses.remove({"name": name, "amount": amount, "category": category})

        table.delete(item)

    update_total()

buttons = tk.Frame(window, bg="#18212F")
buttons.pack(pady=10)

tk.Button(buttons, text="Add Expense", font=("Arial", 12), command=add_expense, bg="#4CAF50", fg="#FFFFFF").grid(row=0, column=0, padx=10)
tk.Button(buttons, text="Delete Selected Expense", font=("Arial", 12), command=delete_expense, bg="#F44336", fg="#FFFFFF").grid(row=0, column=1, padx=10)

window.mainloop()