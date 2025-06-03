import os
import csv
import base64
import getpass
from cryptography.fernet import Fernet

# Constants
KEY_FILE = "key.key"
DATA_FILE = "passwords.csv"
ENCRYPTED_FILE = "passwords.encrypted"

# Generate or load AES key
def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)

# Encrypt file on exit
def encrypt_file(cipher):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        with open(ENCRYPTED_FILE, "wb") as f:
            f.write(encrypted)
        os.remove(DATA_FILE)

# Decrypt file on startup
def decrypt_file(cipher):
    if os.path.exists(ENCRYPTED_FILE):
        with open(ENCRYPTED_FILE, "rb") as f:
            encrypted = f.read()
        decrypted = cipher.decrypt(encrypted)
        with open(DATA_FILE, "wb") as f:
            f.write(decrypted)

# Add new entry
def add_entry(cipher):
    title = input("Title: ")
    password = getpass.getpass("Password: ")
    encrypted_password = cipher.encrypt(password.encode()).decode()
    url = input("URL or App Name: ")
    notes = input("Notes: ")
    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([title, encrypted_password, url, notes])
    print("✅ Entry added.")

# Search for entry
def search_entry():
    title = input("Enter title to search: ")
    found = False
    with open(DATA_FILE, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == title:
                print(f"🔎 Title: {row[0]}\n🔗 URL/App: {row[2]}\n📝 Notes: {row[3]}")
                found = True
                break
    if not found:
        print("❌ Entry not found.")

# Update password
def update_password(cipher):
    title = input("Enter title to update: ")
    updated = False
    rows = []
    with open(DATA_FILE, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == title:
                new_pass = getpass.getpass("New password: ")
                row[1] = cipher.encrypt(new_pass.encode()).decode()
                updated = True
            rows.append(row)
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("✅ Password updated." if updated else "❌ Entry not found.")

# Delete entry
def delete_entry():
    title = input("Enter title to delete: ")
    deleted = False
    rows = []
    with open(DATA_FILE, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != title:
                rows.append(row)
            else:
                deleted = True
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("✅ Entry deleted." if deleted else "❌ Entry not found.")

# Main menu loop
def main():
    cipher = load_or_create_key()
    decrypt_file(cipher)

    while True:
        print("\n--- PASSWORD MANAGER ---")
        print("1. Add New Entry")
        print("2. Search Entry")
        print("3. Update Password")
        print("4. Delete Entry")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry(cipher)
        elif choice == "2":
            search_entry()
        elif choice == "3":
            update_password(cipher)
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            encrypt_file(cipher)
            print("🔐 Data encrypted. Exiting...")
            break
        else:
            print("❗ Invalid choice.")

if __name__ == "__main__":
    main()
