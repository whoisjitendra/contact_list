import tkinter as tk
from tkinter import messagebox

class ContactListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact List")

        
        self.contacts = {}

        
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(root, width=40)
        self.name_entry.pack(pady=5)

        
        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(root, width=40)
        self.phone_entry.pack(pady=5)

        
        add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        add_button.pack(pady=10)

        view_button = tk.Button(root, text="View Contact List", command=self.view_contact_list)
        view_button.pack(pady=5)

        
        search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        search_button.pack(pady=5)

        
        update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        update_button.pack(pady=5)

        
        remove_button = tk.Button(root, text="Remove Contact", command=self.remove_contact)
        remove_button.pack(pady=5)

        
        exit_button = tk.Button(root, text="Exit", command=root.destroy)
        exit_button.pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            if name in self.contacts:
                messagebox.showwarning("Warning", "Contact already exists. Use update to modify.")
            else:
                self.contacts[name] = phone
                messagebox.showinfo("Success", "Contact added successfully.")
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both name and phone number.")

    def view_contact_list(self):
        contact_list = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
        if contact_list:
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts available.")

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.contacts[name]
            messagebox.showinfo("Contact Found", f"{name}: {phone}")
        else:
            messagebox.showinfo("Contact Not Found", "Contact not found.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name in self.contacts:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact updated successfully.")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Contact Not Found", "Contact not found. Use add to create a new contact.")

    def remove_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact removed successfully.")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Contact Not Found", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactListApp(root)
    root.mainloop()
