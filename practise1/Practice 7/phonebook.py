import csv
import psycopg2
from connect import get_connection


def create_table():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                phone VARCHAR(20) NOT NULL UNIQUE
            )
        """)

        conn.commit()
        cur.close()
        print("Table created successfully.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def insert_from_csv():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        with open("contacts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    cur.execute(
                        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                        (row["first_name"], row["phone"])
                    )
                except psycopg2.Error:
                    conn.rollback()
                    conn = get_connection()
                    cur = conn.cursor()
                    print(f"Skipped duplicate or invalid row: {row}")

        conn.commit()
        cur.close()
        print("CSV data inserted successfully.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def insert_from_console():
    first_name = input("Enter first name: ")
    phone = input("Enter phone: ")

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
            (first_name, phone)
        )

        conn.commit()
        cur.close()
        print("Contact inserted successfully.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def update_contact():
    search_name = input("Enter the contact name to update: ")
    print("1. Update first name")
    print("2. Update phone")
    choice = input("Choose: ")

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        if choice == "1":
            new_name = input("Enter new first name: ")
            cur.execute(
                "UPDATE phonebook SET first_name = %s WHERE first_name = %s",
                (new_name, search_name)
            )
        elif choice == "2":
            new_phone = input("Enter new phone: ")
            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE first_name = %s",
                (new_phone, search_name)
            )
        else:
            print("Invalid choice.")
            cur.close()
            conn.close()
            return

        conn.commit()
        cur.close()
        print("Contact updated successfully.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def query_all():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM phonebook ORDER BY id")
        rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No contacts found.")

        cur.close()

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
    finally:
        if conn is not None:
            conn.close()


def query_by_name():
    name = input("Enter name: ")

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM phonebook WHERE first_name ILIKE %s",
            (f"%{name}%",)
        )

        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No matching contacts found.")

        cur.close()

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
    finally:
        if conn is not None:
            conn.close()


def query_by_phone_prefix():
    prefix = input("Enter phone prefix: ")

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM phonebook WHERE phone LIKE %s",
            (prefix + "%",)
        )

        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No matching contacts found.")

        cur.close()

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
    finally:
        if conn is not None:
            conn.close()


def delete_by_name():
    name = input("Enter name to delete: ")

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM phonebook WHERE first_name = %s",
            (name,)
        )

        conn.commit()
        cur.close()
        print("Contact(s) deleted successfully.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def delete_by_phone():
    phone = input("Enter phone to delete: ")

    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM phonebook WHERE phone = %s",
            (phone,)
        )

        conn.commit()
        cur.close()
        print("Contact deleted successfully.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create table")
        print("2. Insert data from CSV")
        print("3. Insert data from console")
        print("4. Update contact")
        print("5. Show all contacts")
        print("6. Query by name")
        print("7. Query by phone prefix")
        print("8. Delete by name")
        print("9. Delete by phone")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            query_all()
        elif choice == "6":
            query_by_name()
        elif choice == "7":
            query_by_phone_prefix()
        elif choice == "8":
            delete_by_name()
        elif choice == "9":
            delete_by_phone()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()