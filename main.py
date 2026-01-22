# A Tkinter GUI desktop application that tests your typing speed.
# © 2026 Ash Hewerdine, HewerDesign.

# Using Tkinter and what you have learnt about building GUI applications with Python, build a desktop app that assesses
# your typing speed. Give the user some sample text and detect how many words they can type per minute.

# The average typing speed is 40 words per minute. But with practice, you can speed up to 100 words per minute.

# If you have more time, you can build your typing speed test into a typing trainer, with high scores and more text
# samples. You can design your program any way you want.

import random
import time
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Typing Speed Assessment")
root.geometry("800x600")
root.option_add("*Label.Font", "consolas 15")
root.option_add("*Button.Font", "consolas 15")

text_options = [
    "The quick brown fox jumps over the lazy dog.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "If Peter Piper picked a peck of pickled peppers, where's the peck of pickled peppers Peter Piper picked?"
]

text_sample = random.choice(text_options).lower()
words_per_minute = float
start_time = 0
entered_text = tk.StringVar()
score = ""


def start_measurement():
    global start_time
    start_time = time.time()
    entry.focus()


def end_measurement():
    global start_time, words_per_minute, score
    if start_time == 0:
        print("Timer not started")
        return

    end_time = time.time()
    elapsed = end_time - start_time
    words = len(text_sample.split())
    words_per_minute = float(words / elapsed * 60)
    score = f"You typed {words} words in {elapsed} seconds. That is equivalent to {words_per_minute} words per minute!"
    print(score)
    score_label = ttk.Label(root, text=score, anchor='center')
    score_label.pack()


def play():
    global start_time, entered_text

    print(text_sample)
    start_measurement()
    entered_text = input("Copy the above text: \n")

    if entered_text.lower() == text_sample:
        end_measurement()
    else:
        print("Wrong input!")



instruction = ttk.Label(root, text="Copy the following text, including punctuation: ", anchor='center')
text_ = ttk.Label(root, text=text_sample, anchor='center')
start_button = ttk.Button(root, text="Start", command=start_measurement)
entry = ttk.Entry(root, textvariable=entered_text)

instruction.pack()
text_.pack()
entry.pack()
start_button.pack()
entry.bind("<Return>", (lambda event: end_measurement()))

root.mainloop()
