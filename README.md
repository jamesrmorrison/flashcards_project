# Flashcard Project

## Introduction

Welcome to the Flashcard Project, a comprehensive platform designed to host, manage, and visualize flashcards across various coding topics. 

The project aims to empower learners in mastering concepts by categorizing flashcards into **Beginner**, **Intermediate**, and **Advanced** levels. This README outlines setup instructions, project structure, and contribution guidelines for users and developers.

Licensed under the MIT License.

## Table of Contents

- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Topics](#topics)
- [The Flashcards App](#the-flashcards-app)
- [Future Roadmap](#future-roadmap)
- [Getting Started](#getting-started)
  - [Setup and Installation](#setup-and-installation)
    - [Global Requirements](#global-requirements)
    - [Installing Dependencies](#installing-dependencies)
    - [Security](#security)
- [Contributing Guidelines](#contributing-guidelines)
  - [Version Control Workflow](#version-control-workflow)
- [Project Structure](#project-structure)
- [FAQs or Common Issues](#faqs-or-common-issues)
- [Reporting Errors or Suggesting Features](#reporting-errors-or-suggesting-features)
- [Conclusion](#conclusion)

## Topics

The current list of topics includes:

- Django
- Docker
- Git
- Numpy
- Pandas
- Python
- SQL

### Upcoming Topics

- Flask
- Machine Learning Basics
- Cloud Computing

## The Flashcards App

- A local Python script for visualizing flashcards from JSON files.
- Flashcards are categorized into Beginner, Intermediate, and Advanced levels for structured learning.
- Modular architecture facilitates easy addition or updating of topics.

### Future Roadmap

- Web-based Flashcard Viewer powered by Django.
- User authentication to track progress and manage personalized settings.
- API integrations to dynamically fetch and update flashcards.
- Modern UI for enhanced flashcard visualizations.

## Getting Started

This section provides a quick overview of how to set up the Flashcard Project on your local machine. Follow the detailed instructions below to get started.

### Setup and Installation

#### Global Requirements

- **Python 3.11 or newer**
- **Pipenv** (optional but recommended for dependency management).

Install `pipenv` using:
```bash
pip install pipenv
```

#### Installing Dependencies

1. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```
   Alternatively, use `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the local testing script to visualize flashcards:
   ```bash
   python flashcards.py
   ```

### Security

To prevent exposing sensitive data, ensure the following entries are included in `.gitignore`:

```plaintext
.env
*.pyc
__pycache__/
db.sqlite3
*.log
.idea/ # PyCharm IDE
.vscode/ # Visual Studio Code IDE
```

## Contributing Guidelines

We welcome contributions! The primary area for contributions is expanding the flashcards dataset or adding new features.

### Version Control Workflow

1. Fork the repository.

2. Clone your fork to your local machine:
   ```bash
   git clone https://github.com/{yourusername}/flashcards_project.git
   ```

3. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Commit your changes:
   ```bash
   git add .
   git commit -m "Add feature or fix description"
   ```

5. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Open a Pull Request via [GitHub](https://github.com/jamesrmorrison/flashcards_project/pulls).

## Project Structure

```plaintext
flashcards_project/
|
├── flashcards_data/             # Directory for JSON files
│   ├── django_flashcards.json   # Django flashcards
│   ├── docker_flashcards.json   # Docker flashcards
│   ├── git_flashcards.json      # Git flashcards
│   ├── numpy_flashcards.json    # Numpy flashcards
│   ├── pandas_flashcards.json   # Pandas flashcards
│   ├── python_flashcards.json   # Python flashcards
│   ├── sql_flashcards.json      # SQL flashcards
│   └── template.json            # Template for building a new topic
│
├── .gitignore                   # Git ignore file
├── flashcard_loader.py          # Local script for adding to flashcards
├── flashcards.py                # Local script for visualizing flashcards
├── LICENSE                      # License (e.g., MIT)
├── README.md                    # Project overview and setup instructions
└── requirements.txt             # Project dependencies
```

## FAQs or Common Issues

### Q: What if `pipenv` doesn't work?

**Possible Solutions:**
- Ensure `pipenv` is installed by running:
  ```bash
  pip install pipenv
  ```
- Use `requirements.txt` as an alternative:
  ```bash
  pip install -r requirements.txt
  ```
- Verify your Python version is 3.11 or newer.

### Q: How do I add new flashcards?

**For an existing topic:**
1. Modify the relevant JSON file in the `flashcards_data/` directory.
2. Use the `flashcard_loader.py` script to incorporate your updates.

**For a new topic:**
1. Create a new JSON file in the `flashcards_data/` directory, using `template.json` as a guide.
2. Use the `flashcard_loader.py` script to add the new topic and associated flashcards.

### Q: How do I run the Django web interface (future feature)?
Stay tuned for updates in the [Future Roadmap](#future-roadmap).

## Reporting Errors or Suggesting Features

We value your feedback! If you encounter any errors in the flashcards or have ideas for new topics or features, here's how you can contribute:

1. **Flagging Errors**:
- Navigate to the [Issues](https://github.com/jamesrmorrison/flashcards_project/issues) section of the repository.
- Create a new issue with the following details:
  - Flashcard topic
  - Error details or incorrect information
  - Suggested fix (optional)

2. **Suggesting New Topics or Features**:
- Use the [Issues](https://github.com/jamesrmorrison/flashcards_project/issues) section to describe your suggestion.
- Alternatively, open a discussion in the [Discussions](https://github.com/jamesrmorrison/flashcards_project/discussions) tab.
- Provide a brief summary of your idea and how it could benefit the project.

3. **Pull Requests**:
- If you’re familiar with Git, feel free to fork the repository, make your changes, and submit a Pull Request for review.

## Conclusion

The Flashcard Project is a robust, modular platform for organizing and visualizing educational flashcards. Contributions are always welcome—if you’ve added something valuable, remember to raise a PR!

Thank you for supporting the growth of this project.

