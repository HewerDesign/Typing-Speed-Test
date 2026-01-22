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

# TODO: Keep track of how long it takes to type the given sample, in seconds. Use the number of words to calculate WPM.
# TODO: Count time from first key-press until enter is hit.

# TODO: Create some preset samples if a suitable length, accessed randomly and printed on screen.

# TODO: Add a textbox to allow the user to copy the sample. Check for errors? Add a time penalty per uncorrected error?


text_samples = [
"The quick brown fox jumps over the lazy dog.",
"How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
"If Peter Piper picked a peck of pickled peppers, where's the peck of pickled peppers Peter Piper picked?"
]

text_sample = random.choice(text_samples)
words_per_minute = float
start_time = 0

def start_measurement():
    global start_time
    start_time = time.time()


def end_measurement():
    global start_time, words_per_minute
    if start_time == 0:
        print("Timer not started")
        return

    end_time = time.time()
    elapsed = end_time - start_time
    words = len(text_sample.split())
    words_per_minute = float(words / elapsed * 60)
    print(f"You typed {words} words in {elapsed} seconds. That is equivalent to {words_per_minute} words per minute!")
    start_time = 0  # Reset

def play():
    global start_time
    print(text_sample)
    start_measurement()
    typing = input("Copy the above text: \n")

    if typing.lower() == text_sample.lower():
        end_measurement()

# root = Tk()
# root.title("Typing Speed Assessment")
#
# mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#
# ttk.Label(mainframe, text=text_sample).grid(column=2, row=2, sticky=(W, E))
#
# root.mainloop()

play()
