import psycopg2
import csv

conn = psycopg2.connect(
    dbname="PhoneBook",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 2:
                continue 
            cur.execute(
                "INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()

#insert_from_csv("contacts.csv")

def update_contact():
    choice = input("What would you like to update? (1 - name, 2 - phone): ")
    if choice == '1':
        old_name = input("Enter the current name: ")
        new_name = input("Enter the new name: ")
        cur.execute(
            "UPDATE PhoneBook SET name = %s WHERE name = %s",
            (new_name, old_name)
        )
    elif choice == '2':
        name = input("Enter the name: ")
        new_phone = input("Enter the new phone number: ")
        cur.execute(
            "UPDATE PhoneBook SET phone = %s WHERE name = %s",
            (new_phone, name)
        )
    conn.commit()

def search_contacts():
    keyword = input("Enter a name or phone number to search: ")
    cur.execute(
        "SELECT * FROM PhoneBook WHERE name ILIKE %s OR phone LIKE %s",
        ('%' + keyword + '%', '%' + keyword + '%')
    )
    results = cur.fetchall()
    for row in results:
        print(row)

def delete_contact():
    keyword = input("Enter the name or phone number to delete: ")
    cur.execute(
        "DELETE FROM PhoneBook WHERE name = %s OR phone = %s",
        (keyword, keyword)
    )
    conn.commit()

def insert_or_update_user():
    name = input("Enter name: ")
    phone = input("Enter phone number (12 digits): ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("User inserted or updated successfully.")

def insert_multiple_users():
    users_data = input("Enter users in format 'name:phone,name:phone,...': ").split(',')
    cur.execute("CALL insert_multiple_users(%s)", (users_data,))
    conn.commit()
    print("Users inserted or updated. Invalid data (if any) was skipped.")

def get_phonebook_paginated():
    limit = int(input("Enter number of records per page: "))
    page = int(input("Enter page number (starting from 0): "))
    offset = page * limit
    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (limit, offset))
    results = cur.fetchall()
    for row in results:
        print(row)

def delete_user_data():
    identifier = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_user_data(%s)", (identifier,))
    conn.commit()
    print("User deleted successfully.")


def main():
    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert data from CSV")
        print("2. Update contact")
        print("3. Search contacts")
        print("4. Delete contact")
        print("5. Insert or update single user")
        print("6. Insert multiple users")
        print("7. Paginated contact list")
        print("8. Delete by stored procedure")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            file_path = input("Enter the path to the CSV file: ")
            insert_from_csv(file_path)
        elif choice == '2':
            update_contact()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            insert_or_update_user()
        elif choice == '6':
            insert_multiple_users()
        elif choice == '7':
            get_phonebook_paginated()
        elif choice == '8':
            delete_user_data()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

main()
conn.close()
