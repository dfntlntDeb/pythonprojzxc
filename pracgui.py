import tkinter as tk
from tkinter import *
import random

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def roll_trait():
    global cntr
    increment = 1
    rolled_trait = roll_trait_once()
    result_var.set(rolled_trait)
    set_trait_color(rolled_trait)
    cntr.set(cntr.get() + increment)
    counter.config(text=f"You rolled {cntr.get()} times.")

def roll_trait_once():
    roll = random.random()
    cumulative_probability = 0.0
    for trait, probability in traits.items():
        cumulative_probability += probability
        if roll < cumulative_probability:
            return trait
    return "No Trait"

def set_trait_color(rolled_trait):
    rarity_colors = {
        "Normal": "black",
        "Rare": "blue",
        "Epic": "purple",
        "Legendary": "orange",
        "Mythical": "red"
    }
    trait_rarity = next((r for r, traits_list in rarity.items() if rolled_trait in traits_list), None)
    if trait_rarity:
        result_entry.config(fg=rarity_colors.get(trait_rarity, "black"))

window = tk.Tk()
window.geometry("700x500")
logo = PhotoImage(file=r"C:\Users\chibi\Python Codes\Practice Codes\imgs\RR_Logo.png")
window.iconphoto(False, logo)
window.title("Anime Defenders Lucky Trait Draw")

center_window(window)

# Define the traits and their roll rates
traits = {
    "Brawler 1": 0.0795,
    "Brawler 2": 0.079,
    "Brawler 3": 0.078,
    "Swiftness 1": 0.07,
    "Swiftness 2": 0.07,
    "Swiftness 3": 0.07,
    "Hunter 1": 0.07,
    "Hunter 2": 0.07,
    "Hunter 3": 0.07,
    "Critical 1": 0.0615,
    "Critical 2": 0.061,
    "Critical 3": 0.06,
    "Prodigy 1": 0.1,
    "Bullseye 1": 0.025,
    "Midas Touch 1": 0.015,
    "Sonic 1": 0.01,
    "Precision 1": 0.008,
    "Requiem 1": 0.002,
    "Almighty 1": 0.999
}

# Define the rarity categories
rarity = {
    "Normal": ["Brawler 1", "Brawler 2", "Brawler 3", "Swiftness 1", "Swiftness 2", "Swiftness 3", "Hunter 1", "Hunter 2", "Hunter 3", "Critical 1", "Critical 2", "Critical 3", "Prodigy 1"],
    "Rare": ["Bullseye 1"],
    "Epic": ["Midas Touch 1"],
    "Legendary": ["Sonic 1", "Precision 1"],
    "Mythical": ["Requiem 1", "Almighty 1"]
}

result_var = tk.StringVar()
result_entry = tk.Entry(window, font=("Segoe UI", 33, "bold"), textvariable=result_var, state="readonly", justify="center")
result_entry.pack(pady="50", padx="50")

reroll_button = tk.Button(window, text="Reroll Trait", font=("Segoe UI", 13, "bold"), fg="white", pady=10, padx=20, borderwidth=3, bg="black", command=roll_trait)
reroll_button.pack()

cntr = tk.IntVar()
counter = tk.Label(window, text=f"You rolled {cntr.get()} times.", font=("Segoe UI", 32, "bold"))
counter.pack(padx=20, pady=20)

window.mainloop()
