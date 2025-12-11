# Workout Tracker (CLI)

A simple Python command-line program for recording workout exercises.
This project is designed to practice core Python skills such as lists, dictionaries,
loops, input handling, and basic error checking.

## Features

- Add exercises with name, stes, reps, and weight
- View all logged exercises
- Simple text-based menu
- Basic input validation using try/except

## How It Works

When the program starts, it displays a menu:

1. Add Exercise – Add any number of exercises
2. View Workout – Display all stored exercises
3. Exit – Close the program

Each exercise is stored as a dictionary inside a list:

{
    "name": "Bench Press",
    "reps": 10,
    "weight": 60
}

## Purpose of This Project

This project helps practice foundational Python concepts:

- Working with lists and dictionaries
- Accepting and validating user input
- Structuring loops and control flow
- Building small, practical programs

## How to Run

python3 workouttracker.py

## Possible Future Improvements

- More usefull functions
- Saving workouts to a file (JSON, CSV, SQLite)

