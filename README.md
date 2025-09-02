# Rental-management-system-using-python
🏠 Rental Management System

This is a simple Rental Management System built with Python. The project helps manage tenant records, track rent payments, and update data in a structured way. This is first year college project level only.

📌 Features

Store tenant details such as room number, name, months paid, and rent amount.
Read tenant records from a text file (rents.txt).
Save (write) updated records back to the file.
Display data in a clean, table-like format.
Prevents manual tracking errors and keeps data organized.

⚙️ How It Works

Data Structure: Each tenant’s record is stored as a dictionary, and all tenant records are collected in a list.

Read Function: Loads data from rents.txt, splits each line, and converts it into a dictionary.

Write Function: Updates rents.txt by writing the list of dictionaries back to the file.

Display Function: Nicely formats tenant data in a readable table format on the console.

📂 File Example (rents.txt)
101,John,2025-08-01,1,August,5000
102,Mary,2025-07-01,2,July-August,9500
