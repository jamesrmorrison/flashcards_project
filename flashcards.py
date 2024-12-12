import json
import os
import random

def load_flashcards(directory):
    """
    Load flashcards from JSON files in the specified directory.

    Args:
        directory (str): Path to the directory containing JSON files.

    Returns:
        dict: A dictionary where keys are topics and values are lists of flashcards.
    """
    flashcards = {}
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            topic = filename.replace('_flashcards.json', '')
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                flashcards[topic] = json.load(file)
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
        print(f"Topic '{topic}' not found.")
        return []

    return [card for card in flashcards[topic] if card.get('level', '').lower() == level.lower()]

def display_flashcard(flashcard):
    """
    Display a flashcard question and its answer.

    Args:
        flashcard (dict): The flashcard to display.
    """
    print("\nQuestion:")
    print(flashcard.get('question', 'No question available'))
    input("Press Enter to reveal the answer...")
    print("Answer:")
    print(flashcard.get('answer', 'No answer available'))

def main():
    """
    Main function to run the flashcard app.
    """
    print("Welcome to the Flashcards App!\n")

    # Load flashcards from the data directory
    data_directory = "flashcards_data"
    flashcards = load_flashcards(data_directory)

    if not flashcards:
        print("No flashcards found. Make sure the 'flashcards_data' directory contains JSON files.")
        return

    while True:
        print("\nAvailable Topics:")
        for i, topic in enumerate(flashcards.keys(), 1):
            print(f"{i}. {topic.capitalize()}")

        topic_choice = input("\nEnter the number of the topic you'd like to study (or 'q' to quit): ").strip()
        if topic_choice.lower() == 'q':
            print("Goodbye! Happy learning!")
            break

        try:
            topic_index = int(topic_choice) - 1
            topic = list(flashcards.keys())[topic_index]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            continue

        print("\nSelect Difficulty Level:")
        levels = ['Beginner', 'Intermediate', 'Advanced']
        for i, level in enumerate(levels, 1):
            print(f"{i}. {level}")

        level_choice = input("Enter the number of the level you'd like to study: ").strip()
        try:
            level_index = int(level_choice) - 1
            level = levels[level_index]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            continue

        cards = get_flashcard_by_level(flashcards, topic, level)
        if not cards:
            print(f"No flashcards found for {topic.capitalize()} at {level} level.")
            continue

        print(f"\nStudying {topic.capitalize()} at {level} level. Press Enter to continue.")
        for card in random.sample(cards, len(cards)):
            display_flashcard(card)

if __name__ == "__main__":
    main()
