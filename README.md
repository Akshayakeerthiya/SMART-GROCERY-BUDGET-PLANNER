# SMART GROCERY BUDGET PLANNER

## Overview

A Python-based command-line application for managing grocery items, tracking expenses, and staying within a defined budget.

## Key Features

* Set and manage grocery budget
* Add, view, update, and remove grocery items
* Calculate and track total grocery expenses
* Check remaining or exceeded budget
* Generate category-wise expense summary
* Classify items as Essential or Optional and provide budget suggestions
* Validate user inputs and handle exceptions
* Save and load grocery data using JSON file handling

## Technologies Used

**Python | Object-Oriented Programming | JSON | File Handling | Exception Handling**

## Commands

* `add` – Add a grocery item
* `view` – View grocery items
* `total` – Calculate total expense
* `budget` – Check budget
* `summary` – View category-wise expenses
* `suggest` – Get budget suggestions
* `update` – Update item price
* `remove` – Remove an item
* `save` – Save data
* `exit` – Exit the application

## Input Validation

The application validates:

* Budget values
* Item names
* Prices
* Categories
* Item priorities
* User commands

Invalid numeric inputs are handled using `try-except` and `ValueError`.

## Data Persistence

Grocery budget and item details are stored in `grocery_data.json`.

The application automatically loads previously saved data when restarted and saves changes made during the session.

## Conclusion

Smart Grocery Budget Planner is a simple Python-based application that helps users manage grocery items, track expenses, and control their grocery budget. The project demonstrates practical use of Object-Oriented Programming, file handling, JSON data storage, input validation, and exception handling in Python.
