import json
import os
import random
import time
import tkinter as tk
from tkinter import messagebox


def load_flashcards(directory):
    """
    Load flashcards from JSON files in the specified directory.

    Args:
        directory (str): Path to the directory containing JSON files.

    Returns:
        dict: A dictionary where keys are topics (subjects) and values are lists of flashcards.
    """
    flashcards = {}
    for filename in os.listdir(directory):
        if filename.endswith('.json') and filename != 'template.json':
            # Capitalize subject name
            subject = filename.replace('_flashcards.json', '').capitalize()
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                flashcards[subject] = json.load(file)
    return flashcards


def get_flashcard_by_level(flashcards, topic, level):
    """
    Retrieve flashcards of a specific level from a topic.

    Args:
        flashcards (dict): The flashcards dictionary.
        topic (str): The topic to select flashcards from.
        level (str): The difficulty level ('Beginner', 'Intermediate', 'Advanced').

    Returns:
        list: A list of flashcards matching the level.
    """
    if topic not in flashcards:
        return []

    return [card for card in flashcards[topic] if card.get('level', '').lower() == level.lower()]


def display_flashcard(flashcard, question_label, answer_label):
    """
    Display the flashcard question and its answer.

    Args:
        flashcard (dict): The flashcard to display.
        question_label (tk.Label): The label to display the question.
        answer_label (tk.Label): The label to display the answer.
    """
    question_label.config(text=flashcard.get('question', 'No question available'))
    answer_label.config(text="")  # Hide answer initially


def reveal_answer(flashcard, answer_label):
    """
    Reveal the answer for the current flashcard.

    Args:
        flashcard (dict): The flashcard whose answer is to be revealed.
        answer_label (tk.Label): The label to display the answer.
    """
    answer_label.config(text=flashcard.get('answer', 'No answer available'))


def next_flashcard(flashcards, topic, level, question_label, answer_label):
    """
    Load the next random flashcard.

    Args:
        flashcards (dict): The dictionary containing all flashcards.
        topic (str): The selected topic.
        level (str): The selected difficulty level.
        question_label (tk.Label): The label to display the question.
        answer_label (tk.Label): The label to display the answer.
    """
    cards = get_flashcard_by_level(flashcards, topic, level)
    if not cards:
        messagebox.showwarning("No Cards", f"No flashcards found for {topic.capitalize()} at {level} level.")
        return

    flashcard = random.choice(cards)
    display_flashcard(flashcard, question_label, answer_label)
    return flashcard


def start_flashcard_session():
    """
    Start the flashcard session with the selected topic and level.
    """
    subject = subject_var.get()  # Corrected variable name
    level = level_var.get()

    # Ensure valid subject and level
    if not subject or not level:
        messagebox.showwarning("Input Error", "Both subject and level must be selected.")
        return

    flashcards = load_flashcards('flashcards_data')
    if not flashcards:
        messagebox.showwarning("No Cards", "No flashcards available. Ensure the data directory is populated.")
        return

    # Set up the first flashcard
    flashcard = next_flashcard(flashcards, subject, level, question_label, answer_label)

    def on_next():
        nonlocal flashcard
        flashcard = next_flashcard(flashcards, subject, level, question_label, answer_label)

    def on_reveal():
        reveal_answer(flashcard, answer_label)

    next_button.config(command=on_next)
    reveal_button.config(command=on_reveal)


def reset_selections():
    """
    Reset subject, level, and clear the question/answer labels.
    """
    subject_var.set("")  # Reset the subject dropdown to empty
    level_var.set("")  # Reset the level dropdown to empty
    question_label.config(text="Question will appear here")  # Clear the question label
    answer_label.config(text="")  # Clear the answer label


# Create the UI
app = tk.Tk()
app.title("Flashcards App")

# Load available subjects (previously called topics) and levels
data_directory = 'flashcards_data'
flashcards = load_flashcards(data_directory)
subjects = list(flashcards.keys())
levels = ['Beginner', 'Intermediate', 'Advanced', 'Expert']

# UI Elements
tk.Label(app, text="Select Subject:").grid(row=0, column=0, padx=5, pady=5)
subject_var = tk.StringVar()
subject_menu = tk.OptionMenu(app, subject_var, "", *subjects)  # Add empty option as the first one
subject_menu.grid(row=0, column=1, padx=5, pady=5)

tk.Label(app, text="Select Level:").grid(row=1, column=0, padx=5, pady=5)
level_var = tk.StringVar()
level_menu = tk.OptionMenu(app, level_var, "", *levels)  # Add empty option as the first one
level_menu.grid(row=1, column=1, padx=5, pady=5)

# Start Session button
start_button = tk.Button(app, text="Start Session", command=start_flashcard_session)
start_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Flashcard display
question_label = tk.Label(app, text="Question will appear here", width=50, height=3, wraplength=400)
question_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

answer_label = tk.Label(app, text="", width=50, height=3, wraplength=400)
answer_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Buttons for Reveal Answer and Next Flashcard
reveal_button = tk.Button(app, text="Reveal Answer", width=20)
reveal_button.grid(row=5, column=0, padx=5, pady=5)

next_button = tk.Button(app, text="Next Flashcard", width=20)
next_button.grid(row=5, column=1, padx=5, pady=5)

# Reset Button
reset_button = tk.Button(app, text="Reset", command=reset_selections)
reset_button.grid(row=6, columnspan=2, padx=5, pady=5)

# Run the app
app.mainloop()
