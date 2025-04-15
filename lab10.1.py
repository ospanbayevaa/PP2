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

def main():
    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert data from CSV")
        print("2. Update contact")
        print("3. Search contacts")
        print("4. Delete contact")
        print("5. Exit")

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
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

main()
