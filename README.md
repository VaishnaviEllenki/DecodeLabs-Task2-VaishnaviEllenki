# DecodeLabs-Task2-VaishnaviEllenki
# 💰 Expense Tracker System

A command-line based Expense Tracker developed using Python that enables users to record, manage, search, and analyze daily expenses using CSV file storage.

## 🚀 Features

- Add new expenses
- View all recorded expenses
- Calculate total expenses
- Search expenses by category
- Delete expenses by date
- Persistent storage using CSV files
- User-friendly menu-driven interface

## 📂 Project Structure

```
Expense-Tracker-Python/
│
├── main.py
├── expenses.csv
└── README.md
```

## 🛠️ Technologies Used

- Python 3
- CSV Module
- OS Module

## ▶️ How to Run

### Prerequisites

- Python 3.x installed on your system

### Steps

1. Clone the repository:

```bash
git clone https://github.com/VaishnaviEllenki/DecodeLabs-Task2-VaishnaviEllenki.git
          
```

2. Navigate to the project directory:

```bash
cd DecodeLabs-Task2-VaishnaviEllenki
```

3. Run the application:

```bash
python main.py
```

## 📖 Functionalities

### 1️⃣ Add Expense

Allows users to add new expense records with:

- Date
- Category
- Amount
- Description

Example:

```text
Date: 11-06-2026
Category: Food
Amount: 250
Description: Lunch
```

---

### 2️⃣ View Expenses

Displays all stored expenses in a readable format.

Example:

```text
Date: 11-06-2026 | Category: Food | ₹250 | Lunch
Date: 12-06-2026 | Category: Travel | ₹500 | Bus Ticket
```

---

### 3️⃣ Total Expense

Calculates and displays the total amount spent.

Example:

```text
💰 Total Expense: ₹750
```

---

### 4️⃣ Search by Category

Allows users to find expenses belonging to a specific category.

Example:

```text
Enter category to search: Food
```

Output:

```text
Date: 11-06-2026 | ₹250 | Lunch
```

---

### 5️⃣ Delete Expense

Removes an expense record based on its date.

Example:

```text
Enter date of expense to delete: 11-06-2026
```

Output:

```text
✅ Expense Deleted!
```

---

### 6️⃣ Exit Application

Safely exits the program.

Example:

```text
Thank You!
```

## 📸 Sample Menu

```text
===== EXPENSE TRACKER =====

1. Add Expense
2. View Expenses
3. Total Expense
4. Search by Category
5. Delete Expense
6. Exit
```

## 🎯 Learning Outcomes

This project helps in understanding:

- Python File Handling
- CSV Operations
- Functions and Modular Programming
- Loops and Conditional Statements
- Data Storage and Retrieval
- CRUD Operations
- Menu-Driven Application Development

## 🌟 Project Highlights

- Beginner-friendly Python project
- Real-world personal finance management application
- Demonstrates file handling and data persistence
- Suitable for academic projects and GitHub portfolios
- Easy to customize and extend with advanced features

## 🔮 Future Enhancements

- Monthly and Yearly Expense Reports
- Budget Tracking and Alerts
- Data Visualization using Matplotlib
- Expense Summary Dashboard
- SQLite Database Integration
- Export Reports to Excel/PDF
- User Authentication System
- GUI Version using Tkinter

## 👩‍💻 Author

**Vaishnavi Ellenki**

Engineering Student | Python Developer | Machine Learning Enthusiast

- GitHub: https://github.com/VaishnaviEllenki
- LinkedIn: https://linkedin.com/in/vaishnaviellenki


⭐ If you found this project useful, consider giving it a star on GitHub!
