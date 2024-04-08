# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 23:16:39 2024

@author: ATANU
"""

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, old_contact, new_contact):
        idx = self.contacts.index(old_contact)
        self.contacts[idx] = new_contact

    def delete_contact(self, contact):
        self.contacts.remove(contact)

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully.")
        elif choice == '2':
            contact_manager.view_contact_list()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_results = contact_manager.search_contact(search_term)
            if search_results:
                print("Search Results:")
                for contact in search_results:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            updated_contact = Contact(name, phone_number, email, address)
            old_contacts = contact_manager.search_contact(name)
            if old_contacts:
                old_contact = old_contacts[0]
                contact_manager.update_contact(old_contact, updated_contact)
                print("Contact updated successfully.")
            else:
                print("Contact not found.")
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contacts_to_delete = contact_manager.search_contact(name)
            if contacts_to_delete:
                contact_manager.delete_contact(contacts_to_delete[0])
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
