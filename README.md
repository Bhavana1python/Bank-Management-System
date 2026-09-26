# 🏦 Banking Information System

A simple **Python-based Banking Information System** that allows users to manage customer bank accounts through a menu-driven console application.

The project uses Python classes and the `pickle` module to store and retrieve customer account records.

## 📌 Features

The application provides the following operations:

1. **Open an Account**
2. **Generate PIN**
3. **Change PIN**
4. **Deposit Money**
5. **Withdraw Money**
6. **Search for Customer**
7. **View Single Customer Details**
8. **View All Customers**
9. **Close an Account**
10. **Exit**

These options are available through the main banking menu.

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **Pickle** for data storage
* Python modules and classes
* File handling
* Exception handling

## 📂 Project Structure

```text
Banking-Information-System/
│
├── BankAccountOpen.py
├── BankCloseAccount.py
├── BankDeposit.py
├── BankMenu.py
├── BankPinGenerateUpdate.py
├── Bankrecords.py
├── BankSearchCustomer.py
├── BankViewCustomers.py
├── BankWithDraw.py
├── BankMainProject.py
├── Banking.pick
└── README.md
```

## 📄 File Description

| File                       | Description                                          |
| -------------------------- | ---------------------------------------------------- |
| `BankMainProject.py`       | Main project file                                    |
| `BankMenu.py`              | Displays the banking menu                            |
| `BankAccountOpen.py`       | Creates new customer accounts                        |
| `Bankrecords.py`           | Reads customer records and checks account uniqueness |
| `BankPinGenerateUpdate.py` | Generates and updates customer PINs                  |
| `BankDeposit.py`           | Handles money deposits                               |
| `BankWithDraw.py`          | Handles money withdrawals                            |
| `BankSearchCustomer.py`    | Searches for a customer using account number         |
| `BankViewCustomers.py`     | Displays individual or all customer details          |
| `BankCloseAccount.py`      | Deletes/closes an existing account                   |
| `Banking.pick`             | Stores customer account records                      |

## 👤 Account Creation

When opening an account, the application collects:

* Account number
* Customer name
* Initial balance
* PIN
* Branch name

The account record is stored as a list and written to the pickle file.

Example record structure:

```text
[Account Number, Customer Name, Balance, PIN, Branch Name]
```

## 💰 Deposit

The deposit feature searches for the customer's account number and adds the entered amount to the existing balance. The updated records are then saved back to the data file.

## 💸 Withdrawal

The withdrawal feature allows money to be withdrawn from an account while attempting to maintain a minimum balance of **500**.

## 🔐 PIN Management

The project provides functionality to:

* Generate a new 4-digit PIN
* Change an existing PIN
* Validate that the PIN contains four digits

The PIN generation code checks whether a PIN already exists before generating one.

## 🔎 Customer Search

Customers can be searched using their account number. The program reports whether the customer record exists.

## 👀 View Customer Details

The application can display details for an individual customer, including:

* Account number
* Customer name
* Balance
* PIN
* Branch name

The individual-view feature masks the displayed PIN with `*` characters.

The application can also display all customer records in tabular form.

## 🗑️ Close Account

The account closure feature searches for the specified account number, removes the matching record, and saves the remaining records back to the pickle file.

## 💾 Data Storage

Customer records are stored using Python's `pickle` module.

The `bankrecord` class loads records from the pickle file and provides a method to check whether an account number is unique.

> **Note:** The current source code uses a local Windows file path for `Banking.pick`. Before running the project on another computer, update the file path to match the local environment.

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installation:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 3. Open the Project Folder

```bash
cd Banking-Information-System
```

### 4. Run the Main Program

Run the project's main Python file:

```bash
python BankMainProject.py
```

If your project uses a different file as the main entry point, run that file instead.

## 🖥️ Example Menu

```text
==================================================
        Banking Information System
==================================================
        1.Open An Account
        2.PIN generate
        3.PIN change
        4.Deposit
        5.Withdraw
        6.Search for customer
        7.view single customer details
        8.View all customers
        9.Close an account
        10.Exit
==================================================
```

## 🎯 Learning Objectives

This project demonstrates practical use of:

* Python classes and objects
* Functions and methods
* Conditional statements
* Loops
* Exception handling
* File handling
* Pickle serialization
* Modular Python programming
* Basic banking operations

## ⚠️ Disclaimer

This is an **educational Python project** created to demonstrate programming concepts.

It is **not intended for real banking or financial transactions**. The current implementation uses local file-based storage and should not be used to store real customer or banking information.

## 👩‍💻 Author

**Bhavana**

### ⭐ If you found this project useful

Feel free to ⭐ star the repository and explore the code to learn more about Python and Object-Oriented Programming.
