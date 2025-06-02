#!/usr/bin/env python3
"""
Prework Study Guide - Interactive CLI Quiz Tool
A beautiful command-line quiz application for programming concepts
"""

import json
import random
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Prompt, Confirm
    from rich.table import Table
    from rich.text import Text
    from rich import box
    from rich.align import Align
except ImportError:
    print("Installing required dependencies...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Prompt, Confirm
    from rich.table import Table
    from rich.text import Text
    from rich import box
    from rich.align import Align

console = Console()

# Quiz questions database
QUIZ_DATA = {
    "data_structures": {
        "name": "Data Structures",
        "questions": [
            {
                "question": "What is the time complexity of accessing an element in an array by index?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct": 0,
                "explanation": "Array access by index is constant time O(1) because arrays store elements contiguously in memory."
            },
            {
                "question": "Which data structure follows LIFO (Last In, First Out) principle?",
                "options": ["Queue", "Stack", "Array", "Linked List"],
                "correct": 1,
                "explanation": "A stack follows LIFO - the last element added is the first one to be removed."
            },
            {
                "question": "What is the space complexity of a binary tree with n nodes?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct": 2,
                "explanation": "A binary tree with n nodes requires O(n) space to store all nodes."
            },
            {
                "question": "In a hash table, what happens when two keys hash to the same index?",
                "options": ["Error occurs", "Collision occurs", "Data is lost", "Array resizes"],
                "correct": 1,
                "explanation": "When two keys hash to the same index, it's called a collision and needs to be resolved."
            },
            {
                "question": "What is the average time complexity for searching in a balanced BST?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "correct": 1,
                "explanation": "In a balanced Binary Search Tree, search operations take O(log n) time on average."
            }
        ]
    },
    "algorithms": {
        "name": "Algorithms",
        "questions": [
            {
                "question": "What is the time complexity of the quicksort algorithm in the average case?",
                "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
                "correct": 1,
                "explanation": "Quicksort has O(n log n) average time complexity, though worst case is O(n²)."
            },
            {
                "question": "Which algorithm technique does binary search use?",
                "options": ["Greedy", "Dynamic Programming", "Divide and Conquer", "Backtracking"],
                "correct": 2,
                "explanation": "Binary search uses divide and conquer by repeatedly splitting the search space in half."
            },
            {
                "question": "What is the space complexity of merge sort?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct": 2,
                "explanation": "Merge sort requires O(n) additional space for the temporary arrays during merging."
            },
            {
                "question": "Which sorting algorithm is stable and has O(n log n) worst-case time complexity?",
                "options": ["Quick Sort", "Heap Sort", "Merge Sort", "Selection Sort"],
                "correct": 2,
                "explanation": "Merge sort is stable (maintains relative order) and has O(n log n) worst-case complexity."
            },
            {
                "question": "What is dynamic programming primarily used for?",
                "options": ["Sorting arrays", "Graph traversal", "Optimization problems", "Memory management"],
                "correct": 2,
                "explanation": "Dynamic programming is used to solve optimization problems by breaking them into overlapping subproblems."
            }
        ]
    },
    "python": {
        "name": "Python Programming",
        "questions": [
            {
                "question": "What is the result of: 3 ** 2?",
                "options": ["6", "9", "5", "8"],
                "correct": 1,
                "explanation": "The ** operator is exponentiation in Python, so 3 ** 2 = 3² = 9."
            },
            {
                "question": "Which Python data type is mutable?",
                "options": ["tuple", "string", "list", "int"],
                "correct": 2,
                "explanation": "Lists are mutable in Python, meaning you can change their contents after creation."
            },
            {
                "question": "What does 'self' represent in Python class methods?",
                "options": ["The class itself", "A global variable", "The instance of the class", "Nothing special"],
                "correct": 2,
                "explanation": "'self' refers to the instance of the class that the method is being called on."
            },
            {
                "question": "What is the correct way to create a dictionary in Python?",
                "options": ["dict = []", "dict = {}", "dict = ()", "dict = <>"],
                "correct": 1,
                "explanation": "Dictionaries in Python are created using curly braces {} or the dict() constructor."
            },
            {
                "question": "What is the difference between '==' and 'is' in Python?",
                "options": ["No difference", "'==' compares values, 'is' compares identity", "'is' compares values, '==' compares identity", "Both compare identity"],
                "correct": 1,
                "explanation": "'==' compares values for equality, while 'is' compares object identity (whether they're the same object)."
            }
        ]
    },
    "big_o": {
        "name": "Big O Notation",
        "questions": [
            {
                "question": "Which complexity grows the fastest?",
                "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
                "correct": 2,
                "explanation": "O(n²) quadratic complexity grows much faster than linear O(n) or logarithmic O(log n)."
            },
            {
                "question": "What is the time complexity of a nested loop where both loops run n times?",
                "options": ["O(n)", "O(log n)", "O(n²)", "O(2n)"],
                "correct": 2,
                "explanation": "Two nested loops, each running n times, results in n × n = O(n²) time complexity."
            },
            {
                "question": "Which operation on a sorted array has O(log n) complexity?",
                "options": ["Linear search", "Binary search", "Insertion", "Deletion"],
                "correct": 1,
                "explanation": "Binary search on a sorted array has O(log n) complexity by eliminating half the search space each step."
            },
            {
                "question": "What is the space complexity of an algorithm that uses a fixed amount of extra space?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
                "correct": 2,
                "explanation": "If an algorithm uses a constant amount of extra space regardless of input size, it's O(1) space."
            },
            {
                "question": "In Big O notation, what do we focus on?",
                "options": ["Best case", "Average case", "Worst case", "All cases equally"],
                "correct": 2,
                "explanation": "Big O notation typically describes the worst-case time or space complexity of an algorithm."
            }
        ]
    }
}

class StudyStats:
    def __init__(self):
        self.stats_file = Path("study_stats.json")
        self.load_stats()
    
    def load_stats(self):
        if self.stats_file.exists():
            with open(self.stats_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                "total_questions": 0,
                "correct_answers": 0,
                "sessions": [],
                "category_stats": {}
            }
    
    def save_stats(self):
        with open(self.stats_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def add_session(self, category: str, score: int, total: int):
        session = {
            "date": datetime.now().isoformat(),
            "category": category,
            "score": score,
            "total": total,
            "percentage": round((score / total) * 100, 1)
        }
        self.data["sessions"].append(session)
        self.data["total_questions"] += total
        self.data["correct_answers"] += score
        
        if category not in self.data["category_stats"]:
            self.data["category_stats"][category] = {"correct": 0, "total": 0}
        
        self.data["category_stats"][category]["correct"] += score
        self.data["category_stats"][category]["total"] += total
        self.save_stats()

class QuizApp:
    def __init__(self):
        self.stats = StudyStats()
        self.current_score = 0
        self.current_total = 0
    
    def display_banner(self):
        banner = Text("🎓 PREWORK STUDY GUIDE 🎓", style="bold blue")
        subtitle = Text("Interactive Programming Quiz", style="italic cyan")
        
        console.print()
        console.print(Align.center(Panel(
            Align.center(f"{banner}\n{subtitle}"),
            box=box.DOUBLE,
            style="bright_blue"
        )))
        console.print()
    
    def show_main_menu(self):
        table = Table(show_header=False, box=box.ROUNDED, style="cyan")
        table.add_column("Option", style="bold yellow", width=4)
        table.add_column("Description", style="white")
        
        table.add_row("1", "📚 Start Quiz by Category")
        table.add_row("2", "🎯 Random Mixed Quiz")
        table.add_row("3", "📊 View Study Statistics")
        table.add_row("4", "❓ Help")
        table.add_row("5", "👋 Exit")
        
        console.print(Panel(table, title="[bold green]Main Menu[/bold green]", border_style="green"))
        return Prompt.ask("\n[bold cyan]Choose an option[/bold cyan]", choices=["1", "2", "3", "4", "5"])
    
    def show_categories(self):
        table = Table(show_header=False, box=box.ROUNDED, style="magenta")
        table.add_column("Option", style="bold yellow", width=4)
        table.add_column("Category", style="white")
        table.add_column("Questions", style="dim white")
        
        categories = list(QUIZ_DATA.keys())
        for i, (key, data) in enumerate(QUIZ_DATA.items(), 1):
            question_count = len(data["questions"])
            table.add_row(str(i), data["name"], f"{question_count} questions")
        
        console.print(Panel(table, title="[bold magenta]Study Categories[/bold magenta]", border_style="magenta"))
        
        choices = [str(i) for i in range(1, len(categories) + 1)]
        choice = Prompt.ask("\n[bold magenta]Select a category[/bold magenta]", choices=choices)
        return categories[int(choice) - 1]
    
    def run_quiz(self, category_key: str, num_questions: Optional[int] = None):
        category = QUIZ_DATA[category_key]
        questions = category["questions"].copy()
        random.shuffle(questions)
        
        if num_questions:
            questions = questions[:num_questions]
        
        self.current_score = 0
        self.current_total = len(questions)
        
        console.print(f"\n[bold green]Starting {category['name']} Quiz![/bold green]")
        console.print(f"[dim]You'll answer {len(questions)} questions[/dim]\n")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True,
        ) as progress:
            task = progress.add_task("Loading quiz...", total=None)
            time.sleep(1)
        
        for i, question in enumerate(questions, 1):
            self.ask_question(question, i, len(questions))
        
        self.show_quiz_results(category['name'])
        self.stats.add_session(category['name'], self.current_score, self.current_total)
    
    def ask_question(self, question: dict, current: int, total: int):
        console.print(f"\n[bold blue]Question {current}/{total}[/bold blue]")
        console.print(Panel(
            question["question"],
            title="[bold yellow]❓ Question[/bold yellow]",
            border_style="yellow"
        ))
        
        # Display options
        table = Table(show_header=False, box=None, style="white")
        for i, option in enumerate(question["options"], 1):
            table.add_row(f"[bold cyan]{i}.[/bold cyan]", option)
        
        console.print(table)
        
        # Get user answer
        choices = [str(i) for i in range(1, len(question["options"]) + 1)]
        answer = Prompt.ask("\n[bold cyan]Your answer[/bold cyan]", choices=choices)
        user_choice = int(answer) - 1
        
        # Check answer
        if user_choice == question["correct"]:
            self.current_score += 1
            console.print("[bold green]✅ Correct![/bold green]")
        else:
            correct_option = question["options"][question["correct"]]
            console.print(f"[bold red]❌ Wrong! The correct answer is: {correct_option}[/bold red]")
        
        # Show explanation
        console.print(f"[dim italic]💡 {question['explanation']}[/dim italic]")
        
        if current < total:
            Prompt.ask("\n[dim]Press Enter to continue...[/dim]", default="")
    
    def show_quiz_results(self, category_name: str):
        percentage = round((self.current_score / self.current_total) * 100, 1)
        
        if percentage >= 80:
            emoji = "🎉"
            color = "green"
            message = "Excellent work!"
        elif percentage >= 60:
            emoji = "👍"
            color = "yellow"
            message = "Good job!"
        else:
            emoji = "📚"
            color = "red"
            message = "Keep studying!"
        
        result_text = f"""
{emoji} Quiz Complete! {emoji}

Category: {category_name}
Score: {self.current_score}/{self.current_total}
Percentage: {percentage}%

{message}
        """
        
        console.print(Panel(
            result_text.strip(),
            title=f"[bold {color}]Results[/bold {color}]",
            border_style=color
        ))
    
    def show_statistics(self):
        if self.stats.data["total_questions"] == 0:
            console.print("[yellow]No quiz data yet! Take some quizzes first.[/yellow]")
            return
        
        overall_percentage = round((self.stats.data["correct_answers"] / self.stats.data["total_questions"]) * 100, 1)
        
        # Overall stats
        stats_table = Table(title="📊 Overall Statistics", box=box.ROUNDED)
        stats_table.add_column("Metric", style="cyan")
        stats_table.add_column("Value", style="white")
        
        stats_table.add_row("Total Questions", str(self.stats.data["total_questions"]))
        stats_table.add_row("Correct Answers", str(self.stats.data["correct_answers"]))
        stats_table.add_row("Overall Accuracy", f"{overall_percentage}%")
        stats_table.add_row("Quiz Sessions", str(len(self.stats.data["sessions"])))
        
        console.print(stats_table)
        
        # Category breakdown
        if self.stats.data["category_stats"]:
            console.print("\n")
            category_table = Table(title="📈 Category Performance", box=box.ROUNDED)
            category_table.add_column("Category", style="magenta")
            category_table.add_column("Correct", style="green")
            category_table.add_column("Total", style="white")
            category_table.add_column("Accuracy", style="cyan")
            
            for category, stats in self.stats.data["category_stats"].items():
                accuracy = round((stats["correct"] / stats["total"]) * 100, 1)
                category_table.add_row(
                    category,
                    str(stats["correct"]),
                    str(stats["total"]),
                    f"{accuracy}%"
                )
            
            console.print(category_table)
        
        # Recent sessions
        if self.stats.data["sessions"]:
            console.print("\n")
            recent_table = Table(title="🕒 Recent Sessions (Last 5)", box=box.ROUNDED)
            recent_table.add_column("Date", style="dim white")
            recent_table.add_column("Category", style="magenta")
            recent_table.add_column("Score", style="cyan")
            recent_table.add_column("Accuracy", style="green")
            
            recent_sessions = self.stats.data["sessions"][-5:]
            for session in reversed(recent_sessions):
                date = datetime.fromisoformat(session["date"]).strftime("%Y-%m-%d %H:%M")
                recent_table.add_row(
                    date,
                    session["category"],
                    f"{session['score']}/{session['total']}",
                    f"{session['percentage']}%"
                )
            
            console.print(recent_table)
    
    def show_help(self):
        help_text = """
[bold cyan]How to Use the Study Quiz Tool:[/bold cyan]

🎯 [bold]Quiz Modes:[/bold]
   • Category Quiz: Focus on specific topics
   • Mixed Quiz: Random questions from all categories

📚 [bold]Categories Available:[/bold]
   • Data Structures: Arrays, stacks, queues, trees, etc.
   • Algorithms: Sorting, searching, complexity analysis
   • Python Programming: Syntax, data types, OOP concepts
   • Big O Notation: Time and space complexity

📊 [bold]Statistics:[/bold]
   • Track your progress over time
   • See performance by category
   • Review recent quiz sessions

💡 [bold]Tips:[/bold]
   • Take quizzes regularly to reinforce learning
   • Focus on categories where you score lower
   • Read explanations carefully after each question
   • Use this tool as part of your interview preparation
        """
        
        console.print(Panel(help_text.strip(), title="[bold blue]Help[/bold blue]", border_style="blue"))
    
    def run_mixed_quiz(self):
        num_questions = int(Prompt.ask(
            "[bold cyan]How many questions?[/bold cyan]",
            choices=["5", "10", "15", "20"],
            default="10"
        ))
        
        all_questions = []
        for category_key, category_data in QUIZ_DATA.items():
            for question in category_data["questions"]:
                question_copy = question.copy()
                question_copy["category"] = category_data["name"]
                all_questions.append(question_copy)
        
        random.shuffle(all_questions)
        selected_questions = all_questions[:num_questions]
        
        self.current_score = 0
        self.current_total = len(selected_questions)
        
        console.print(f"\n[bold green]Starting Mixed Quiz![/bold green]")
        console.print(f"[dim]{num_questions} random questions from all categories[/dim]\n")
        
        for i, question in enumerate(selected_questions, 1):
            console.print(f"[dim]Category: {question['category']}[/dim]")
            self.ask_question(question, i, len(selected_questions))
        
        self.show_quiz_results("Mixed Topics")
        self.stats.add_session("Mixed Topics", self.current_score, self.current_total)
    
    def run(self):
        self.display_banner()
        
        while True:
            try:
                choice = self.show_main_menu()
                
                if choice == "1":
                    category = self.show_categories()
                    self.run_quiz(category)
                    
                elif choice == "2":
                    self.run_mixed_quiz()
                    
                elif choice == "3":
                    self.show_statistics()
                    
                elif choice == "4":
                    self.show_help()
                    
                elif choice == "5":
                    console.print("\n[bold green]Thanks for studying! Keep up the great work! 🎓[/bold green]")
                    break
                
                console.print("\n" + "="*50 + "\n")
                
            except KeyboardInterrupt:
                console.print("\n\n[bold yellow]Quiz interrupted. See you next time![/bold yellow]")
                break
            except Exception as e:
                console.print(f"\n[bold red]An error occurred: {e}[/bold red]")
                console.print("[dim]Please try again or restart the application.[/dim]")

def main():
    app = QuizApp()
    app.run()

if __name__ == "__main__":
    main()