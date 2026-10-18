
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Day 5 - Countdown Timer")
window.geometry("420x400")
window.configure(bg="#18212F")
window.resizable(False, False)

remaining_seconds = 0
timer_running = False
timer_job = None


def update_display():
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")


def countdown():
    global remaining_seconds, timer_running, timer_job

    if not timer_running:
        return

    if remaining_seconds > 0:
        remaining_seconds -= 1
        update_display()
        timer_job = window.after(1000, countdown)
    else:
        timer_running = False
        timer_job = None
        timer_label.config(fg="#F87171")
        message_label.config(text="Time is up!")
        window.bell()


def start_timer():
    global remaining_seconds, timer_running

    if timer_running:
        return

    if remaining_seconds <= 0:
        try:
            minutes = int(minutes_entry.get())

            if minutes < 1:
                raise ValueError

            remaining_seconds = minutes * 60
            update_display()

        except ValueError:
            messagebox.showerror(
                "Invalid time",
                "Enter a whole number of minutes (at least 1)."
            )
            return

    timer_running = True
    timer_label.config(fg="#2DD4BF")
    message_label.config(text="Timer running...")
    countdown()


def pause_timer():
    global timer_running, timer_job

    timer_running = False

    if timer_job is not None:
        window.after_cancel(timer_job)
        timer_job = None

    message_label.config(text="Timer paused")


def reset_timer():
    global remaining_seconds, timer_running, timer_job

    timer_running = False

    if timer_job is not None:
        window.after_cancel(timer_job)
        timer_job = None

    try:
        minutes = int(minutes_entry.get())
        if minutes < 1:
            raise ValueError
        remaining_seconds = minutes * 60
    except ValueError:
        remaining_seconds = 0

    timer_label.config(fg="#2DD4BF")
    message_label.config(text="Ready when you are!")
    update_display()


title = tk.Label(
    window,
    text="COUNTDOWN TIMER",
    font=("Arial", 19, "bold"),
    bg="#18212F",
    fg="white"
)
title.pack(pady=(25, 15))

timer_label = tk.Label(
    window,
    text="00:00",
    font=("Consolas", 54, "bold"),
    bg="#18212F",
    fg="#2DD4BF"
)
timer_label.pack(pady=10)

message_label = tk.Label(
    window,
    text="Enter minutes below",
    font=("Arial", 11),
    bg="#18212F",
    fg="#CBD5E1"
)
message_label.pack(pady=5)

minutes_entry = tk.Entry(
    window,
    font=("Arial", 13),
    justify="center",
    width=10
)
minutes_entry.insert(0, "1")
minutes_entry.pack(pady=10)

buttons = tk.Frame(window, bg="#18212F")
buttons.pack(pady=15)

tk.Button(
    buttons,
    text="Start",
    command=start_timer,
    bg="#14B8A6",
    fg="#102027",
    font=("Arial", 11, "bold"),
    width=8
).grid(row=0, column=0, padx=5)

tk.Button(
    buttons,
    text="Pause",
    command=pause_timer,
    bg="#FBBF24",
    fg="#18212F",
    font=("Arial", 11, "bold"),
    width=8
).grid(row=0, column=1, padx=5)

tk.Button(
    buttons,
    text="Reset",
    command=reset_timer,
    bg="#F87171",
    fg="#18212F",
    font=("Arial", 11, "bold"),
    width=8
).grid(row=0, column=2, padx=5)

window.mainloop()
