import tkinter as tk
from tkinter import messagebox
import json
import os

def load_flashcards(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as file:
        return json.load(file)

def save_flashcards(filepath, flashcards):
    with open(filepath, 'w') as file:
        json.dump(flashcards, file, indent=4)

def add_flashcard(filepath, flashcard):
    flashcards = load_flashcards(filepath)
    flashcards.append(flashcard)
    save_flashcards(filepath, flashcards)

def get_existing_options(data_directory):
    subjects = set()
    topics = {}
    levels = ["Beginner", "Intermediate", "Advanced"]
    categories = ["Concepts", "Commands", "Workflows"]
    for filename in os.listdir(data_directory):
        if filename.endswith('.json'):
            flashcards = load_flashcards(os.path.join(data_directory, filename))
            for card in flashcards:
                subject = card.get('subject', '')
                topic = card.get('topic', '')
                subjects.add(subject)
                if subject not in topics:
                    topics[subject] = set()
                topics[subject].add(topic)
    return list(subjects), topics, levels, list(categories)

def update_topics(*args):
    selected_subject = subject_var.get()
    topic_menu['menu'].delete(0, 'end')
    new_topics = topics.get(selected_subject, [])
    for topic in new_topics:
        topic_menu['menu'].add_command(label=topic, command=tk._setit(topic_var, topic))
    topic_var.set('')

def submit_flashcard():
    subject = subject_var.get() if subject_var.get() else new_subject_entry.get()
    level = level_var.get()
    category = category_var.get()
    topic = topic_var.get() if topic_var.get() else new_topic_entry.get()
    question = question_entry.get()
    answer = answer_entry.get()

    if not subject or not topic or not level or not category or not question or not answer:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    filepath = f'flashcards_data/{subject}_flashcards.json'
    new_flashcard = {
        "subject": subject,
        "level": level,
        "category": category,
        "topic": topic,
        "question": question,
        "answer": answer
    }
    add_flashcard(filepath, new_flashcard)
    messagebox.showinfo("Success", f"Flashcard added to {filepath}")

data_directory = 'flashcards_data'
subjects, topics, levels, categories = get_existing_options(data_directory)

app = tk.Tk()
app.title("Add Flashcard")

padding = {'padx': 5, 'pady': 5}

tk.Label(app, text="Subject:").grid(row=0, column=0, **padding)
subject_var = tk.StringVar(app)
subject_var.trace('w', update_topics)
subject_menu = tk.OptionMenu(app, subject_var, *subjects)
subject_menu.grid(row=0, column=1, **padding)
tk.Label(app, text="Or New Subject:").grid(row=0, column=2, **padding)
new_subject_entry = tk.Entry(app)
new_subject_entry.grid(row=0, column=3, **padding)

tk.Label(app, text="Level:").grid(row=1, column=0, **padding)
level_var = tk.StringVar(app)
level_menu = tk.OptionMenu(app, level_var, *levels)
level_menu.grid(row=1, column=1, **padding)

tk.Label(app, text="Category:").grid(row=2, column=0, **padding)
category_var = tk.StringVar(app)
category_menu = tk.OptionMenu(app, category_var, *categories)
category_menu.grid(row=2, column=1, **padding)

tk.Label(app, text="Topic:").grid(row=3, column=0, **padding)
topic_var = tk.StringVar(app)
topic_menu = tk.OptionMenu(app, topic_var, '')
topic_menu.grid(row=3, column=1, **padding)
tk.Label(app, text="Or New Topic:").grid(row=3, column=2, **padding)
new_topic_entry = tk.Entry(app)
new_topic_entry.grid(row=3, column=3, **padding)

tk.Label(app, text="Question:").grid(row=4, column=0, **padding)
question_entry = tk.Entry(app, width=50)
question_entry.grid(row=4, column=1, columnspan=3, **padding)

tk.Label(app, text="Answer:").grid(row=5, column=0, **padding)
answer_entry = tk.Entry(app, width=50)
answer_entry.grid(row=5, column=1, columnspan=3, **padding)

submit_button = tk.Button(app, text="Add Flashcard", command=submit_flashcard)
submit_button.grid(row=6, columnspan=4, **padding)

app.mainloop()