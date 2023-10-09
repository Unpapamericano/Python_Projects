# Python_Projects
# Ranked-Choice Voting using the Tideman Method

This is a C program for conducting ranked-choice voting elections based on the Tideman method. It allows you to calculate the winner of an election, taking into account voter preferences and ensuring that the elected candidate has majority support.

## Table of Contents

- [Introduction](#introduction)
- [How to Use](#how-to-use)
- [File Structure](#file-structure)
- [Function Descriptions](#function-descriptions)

## Introduction

Ranked-choice voting is a fair and inclusive method of conducting elections. This program calculates the winner by following these steps:
1. Collecting and recording voter preferences.
2. Determining pairs of candidates where one is preferred over the other.
3. Sorting the pairs by the strength of victory.
4. Locking pairs into the candidate graph to prevent cycles.
5. Printing the winner of the election.

## How to Use

To use this program, follow these steps:

1. "Compile the program using a C compiler (e.g., `gcc tideman.c -o tideman`)."
2. Run the compiled program, passing the list of candidates as command-line arguments (e.g., `./tideman candidate1 candidate2 candidate3`).
3. Enter the number of voters and their ranked preferences when prompted.
4. The program will calculate the winner and display the result.

## File Structure

- `tideman.c`: The main source code file containing the program's logic.
- `cs50.h`: A library for handling user input (included in the program).
- `stdio.h`: A standard input/output library (included in the program).
- Other header files and function implementations for sorting and checking cycles.

## Function Descriptions

Here are some key functions in the code:

- `vote(int rank, string name, int ranks[])`: Updates voter ranks based on their preferences.
- `record_preferences(int ranks[])`: Records voter preferences and updates the `preferences` array.
- `add_pairs()`: Records pairs of candidates where one is preferred over the other.
- `sort_pairs()`: Sort
