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

# TODO: Keep track of how long it takes to type the given sample, in seconds. Use the number of words to calculate WPM.
# TODO: Count time from first key-press until enter is hit.

# TODO: Create some preset samples if a suitable length, accessed randomly and printed on screen.

# TODO: Add a textbox to allow the user to copy the sample. Check for errors? Add a time penalty per uncorrected error?

words_per_minute = float

text_samples = [
"The quick brown fox jumps over the lazy dog",
"How much wood would a woodchuck chuck if a woodchuck could chuck wood"
]

text_sample = random.choice(text_samples)

def wpm():
    global words_per_minute
    words = len(text_sample.split())
    end = time.time()
    time_taken = end - start
    words_per_minute = float(words / time_taken * 60)
    print(f"You typed {words} words in {time_taken} seconds. That is equivalent to {words_per_minute} words per minute!")

print(text_sample)
start = time.time()
typing = input("Copy the above text: \n")

if typing.lower() == text_sample.lower():
    wpm()
