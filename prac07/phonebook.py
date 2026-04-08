from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100),
        phone VARCHAR(20) UNIQUE
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

create_table()

from connect import connect
from your_functions_file import *

def menu():
    while True:
        print("\nPhoneBook Menu:")
        print("1. Import from CSV")
        print("2. Add contact")
        print("3. View contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            filter_val = input("Filter (optional): ")
            query_contacts(filter_val)
        elif choice == "4":
            old = input("Old name: ")
            new_name = input("New name (or leave empty): ")
            new_phone = input("New phone (or leave empty): ")
            update_contact(old, new_name or None, new_phone or None)
        elif choice == "5":
            val = input("Enter name or phone to delete: ")
            delete_contact(val)
        elif choice == "0":
            break

menu()