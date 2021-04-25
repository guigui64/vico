import tkinter as tk


def gui():
    window = tk.Tk()
    greeting = tk.Label(text="Greetings, user!")
    greeting.pack()
    window.mainloop()
