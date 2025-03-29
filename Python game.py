import tkinter as tk
import random
import time
from tkinter import messagebox, Toplevel

# List of sports-related words with hints
words_with_hints = {
    "football": "Played with a round ball on a field, goals are scored.",
    "basketball": "Played with an orange ball, involves shooting into a hoop.",
    "cricket": "A bat-and-ball game with wickets and overs.",
    "tennis": "Played with a racket and a yellow ball on a court.",
    "badminton": "A fast-paced game played with a shuttlecock.",
    "hockey": "A game played with sticks and a puck/ball on ice or field.",
    "baseball": "A bat-and-ball sport with bases and home runs.",
    "golf": "Played on a course with holes, involves clubs and a small ball.",
    "volleyball": "Played with a net and a ball, involves spiking.",
    "rugby": "A tough game involving an oval ball and tackles."
}

# Choose a random word and its hint
word, hint = random.choice(list(words_with_hints.items()))
word = word.upper()
guessed_word = ["_" for _ in word]
attempts = 6

# Function to update the displayed word with animation
def animate_text(label, text, delay=0.05):
    label.config(text="")
    for char in text:
        label.config(text=label.cget("text") + char)
        root.update()
        time.sleep(delay)

# Function to show a popup message
def show_popup(title, message):
    popup = Toplevel(root)
    popup.title(title)
    popup.geometry("300x150")
    tk.Label(popup, text=message, font=("Arial", 14), wraplength=280).pack(pady=10)
    tk.Button(popup, text="OK", command=popup.destroy, font=("Arial", 12)).pack(pady=5)
    popup.transient(root)
    popup.grab_set()
    root.wait_window(popup)

# Function to update the displayed word
def update_display():
    word_label.config(text=" ".join(guessed_word))
    attempts_label.config(text=f"Attempts left: {attempts}")
    hint_label.config(text=f"Hint: {hint}")

# Function to handle letter guessing
def guess_letter():
    global attempts
    letter = entry.get().upper()
    entry.delete(0, tk.END)
    
    if len(letter) != 1 or not letter.isalpha():
        show_popup("Invalid Input", "Please enter a single letter.")
        return
    
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed_word[i] = letter
    else:
        attempts -= 1
    
    animate_text(word_label, " ".join(guessed_word))
    update_display()
    check_game_status()

# Function to check win/loss condition
def check_game_status():
    if "_" not in guessed_word:
        animate_text(word_label, "You Win!", delay=0.1)
        show_popup("Congratulations!", "You guessed the word!")
        root.quit()
    elif attempts == 0:
        animate_text(word_label, f"Game Over! The word was {word}", delay=0.1)
        show_popup("Game Over", f"You lost! The word was {word}")
        root.quit()

# GUI Setup
root = tk.Tk()
root.title("Hangman - Sports Edition")
root.geometry("400x350")

tk.Label(root, text="Guess the Sports Word:", font=("Arial", 14)).pack(pady=10)
word_label = tk.Label(root, text=" ".join(guessed_word), font=("Arial", 18, "bold"))
word_label.pack()

attempts_label = tk.Label(root, text=f"Attempts left: {attempts}", font=("Arial", 12))
attempts_label.pack()

hint_label = tk.Label(root, text=f"Hint: {hint}", font=("Arial", 12, "italic"))
hint_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

tk.Button(root, text="Guess", command=guess_letter, font=("Arial", 12)).pack()

update_display()
root.mainloop()
