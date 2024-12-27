import sqlite3
import sys


# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            age INTEGER
        )
    ''')
    conn.commit()
    conn.close()


def create_user(username, email, age):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, age) VALUES (?, ?, ?)', (username, email, age))
        conn.commit()
        print("User created successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def read_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users


def update_user(user_id, username=None, email=None, age=None):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    if not user:
        print("User not found!")
        conn.close()
        return

    username = username or user[1]
    email = email or user[2]
    age = age or user[3]

    try:
        cursor.execute('UPDATE users SET username = ?, email = ?, age = ? WHERE id = ?',
                       (username, email, age, user_id))
        conn.commit()
        print("User updated successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    if cursor.rowcount > 0:
        print("User deleted successfully!")
    else:
        print("User not found!")
    conn.commit()
    conn.close()


def main():
    init_db()

    while True:
        print("\nUser Management CLI")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            age = input("Enter age: ")
            create_user(username, email, int(age))
        elif choice == '2':
            users = read_users()
            if users:
                print("\nID | Username | Email | Age")
                for user in users:
                    print(f"{user[0]} | {user[1]} | {user[2]} | {user[3]}")
            else:
                print("No users found.")
        elif choice == '3':
            user_id = int(input("Enter user ID to update: "))
            print("Leave fields empty to keep current values.")
            username = input("Enter new username: ") or None
            email = input("Enter new email: ") or None
            age = input("Enter new age: ") or None
            update_user(user_id, username, email, int(age) if age else None)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
