import tkinter as tk
import random

window = tk.Tk()
window.title("Dice Rolling Simulator")
window.geometry("400x300")
window.config(bg="#18212F")

rolls = 0

#Dice faces using Unicode characters
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

title_label = tk.Label(window, text="Dice Rolling Simulator", font=("Helvetica", 16, "bold"), bg="#18212F", fg="#F5F5F5")
title_label.pack(pady=10)

dice_label = tk.Label(window, text="", font=("Helvetica", 100), bg="#18212F", fg="#F5F5F5")
dice_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#18212F", fg="#F5F5F5")
result_label.pack(pady=10)

counter_label = tk.Label(window, text=f"Total Rolls: {rolls}", font=("Helvetica", 12), bg="#f0f0f0")
counter_label.pack(pady=5)

def roll_dice():
    global rolls
    rolls += 1
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    dice_label.config(text=f"{dice_faces[die1]} {dice_faces[die2]}")
    result_label.config(text=f"Roll {rolls}: {total}")
    counter_label.config(text=f"Total Rolls: {rolls}")

roll_button = tk.Button(window, text="Roll Dice", font=("Helvetica", 14), command=roll_dice, bg="#4CAF50", fg="white")
roll_button.pack(pady=10)

window.mainloop()
