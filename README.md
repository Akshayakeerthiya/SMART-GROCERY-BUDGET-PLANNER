# SMART GROCERY BUDGET PLANNER

## Overview

A Python-based grocery budget management application developed using **Object-Oriented Programming** and later converted into a **Streamlit web application** for an interactive user interface.

The application helps users manage grocery items, track expenses, and stay within their monthly budget.

## Live Demo

🔗 [SMART GROCERY BUDGET PLANNER – LIVE APP](https://smart-grocery-budget-planner-pw6rw3aose2ukuw5hsxv6r.streamlit.app/)

## Key Features

* Set and manage monthly grocery budget
* Add, view, update, and remove grocery items
* Calculate and track total grocery expenses
* Check remaining or exceeded budget
* Generate category-wise expense summary
* Classify items as Essential or Optional
* Provide suggestions when the budget is exceeded
* Validate user inputs
* Save and load grocery data using JSON file handling
* Interactive web interface using Streamlit

## Technologies Used

**Python | Object-Oriented Programming | Streamlit | JSON | File Handling | Exception Handling**

## Application Development

The project was initially developed as a **Python command-line application** using `input()` and `print()` for user interaction.

It was later converted into a **Streamlit web application** to provide an interactive browser-based interface.

### Development Flow

**Python OOP → Command-Line Application → Streamlit Web Application**

## Streamlit Interface

The Streamlit application provides:

* Monthly budget management
* Grocery item input
* Grocery item table
* Expense summary
* Budget status
* Category-wise expense summary
* Budget suggestions
* Update item price
* Remove grocery items

## Data Persistence

Grocery budget and item details are stored in `grocery_data.json`.

The application loads previously saved data when started and saves changes made by the user.

## Project Structure

```text
SMART-GROCERY-BUDGET-PLANNER/
│
├── app.py
├── grocery.py
├── grocery_data.json
├── requirements.txt
├── README.md
└── .gitignore
```

## Conclusion

Smart Grocery Budget Planner demonstrates the practical use of **Python OOP, Streamlit, JSON data storage, file handling, input validation, and exception handling**.

The project also demonstrates the process of converting a **command-line Python application into an interactive Streamlit web application**.
