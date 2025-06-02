# 🎓 Prework Study Guide

# Prework Study Guide

A command-line quiz application for programming fundamentals and technical interview preparation.

## What it does

Interactive quiz tool covering:
- Data Structures (arrays, stacks, queues, trees, hash tables)
- Algorithms (sorting, searching, complexity analysis)  
- Python Programming (syntax, data types, OOP)
- Big O Notation (time and space complexity)

Features progress tracking, detailed explanations, and colorful terminal interface.

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Myrmecology/prework-study-guide.git
cd Prework-Study-Guide
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to run

```bash
python quiz_app.py
```

## Usage

When you run the application, you'll see a menu with these options:

1. **Start Quiz by Category** - Choose specific topics (Data Structures, Algorithms, etc.)
2. **Random Mixed Quiz** - Get random questions from all categories
3. **View Study Statistics** - See your progress and performance over time
4. **Help** - Instructions and tips
5. **Exit** - Close the application

### During a quiz:
- Answer multiple choice questions by typing 1, 2, 3, or 4
- Get immediate feedback with explanations
- See your final score and percentage

### Statistics tracking:
- Overall accuracy rate
- Performance by category
- Session history with timestamps
- All data saved locally in `study_stats.json`

## Quick start example

```bash
# Install and run
pip install rich
python quiz_app.py

# Choose option 1 for category quiz
# Select a category (e.g., Data Structures)
# Answer the questions
# View your results
```

## Adding questions

To add more questions, edit the `QUIZ_DATA` dictionary in `quiz_app.py`. Each question needs:
- `question`: The question text
- `options`: List of 4 possible answers
- `correct`: Index of correct answer (0-3)
- `explanation`: Why the answer is correct

## License

MIT License - feel free to use and modify.
Happy coding