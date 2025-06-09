# Contact Manager
A clean and simple Python project to manage contacts using Object-Oriented Programming (OOP) and JSON for persistent storage.

This project demonstrates essential software engineering principles such as:
- Modular design
- File I/O
- Basic data management
- JSON serialization
- Command-line interaction
  
# Features
•	Add new contacts (name, number, email)
•	Prevent duplicate entries
•	Display all saved contacts
•	 Search by name (case-insensitive)
•	 Delete a contact
•	 Save (backup) contact list to a `.json` file
•	 Load contacts from a JSON file (if provided)


# How to Use
1. Clone the repo:
git clone https://github.com/maryamkhosravii/contactmanager.git

2. Run Example:
from contact_manager import ContactManager
cm = ContactManager()  # or ContactManager("contacts.json")
cm.add("Alice", "09121234567", "alice@example.com")
cm.display()
cm.search("Ali")
cm.delete("Alice")
cm.backup()


# Example Output
Contact Alice has been added.
Contact List:
Name: Alice | Number: 09121234567 | Email: alice@example.com
Searching finished
[{'name': 'Alice', 'number': '09123456789', 'email': 'alice@example.com'}]
Contact Alice has been deleted.
Backup Done.


# Ideas for Future Improvements
•	 CLI interface with argparse
•	 Web interface using Flask or FastAPI
•	 Save contacts to SQLite instead of JSON
•	 Unit testing with pytest


# Author
Made with ❤️ by Maryam Khosravi
GitHub: https://github.com/maryamkhosravii

