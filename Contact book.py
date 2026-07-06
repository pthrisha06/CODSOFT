contacts = []

def add_contact():
    print("\n Add Contact ")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("\n Contact Added Successfully!\n")


def view_contacts():
    print("\n--- Contact List ---")

    if len(contacts) == 0:
        print("No contacts found.\n")
    else:
        print("-" * 50)
        print(f"{'Name':<20}{'Phone Number'}")
        print("-" * 50)

        for contact in contacts:
            print(f"{contact['name']:<20}{contact['phone']}")

        print("-" * 50)

def search_contact():
    print("\n Search Contact ")
    search = input("Enter Name or Phone Number: ")

    found = False

    for contact in contacts:
        if (contact["name"].lower() == search.lower() or
                contact["phone"] == search):

            print("\nContact Found")
            print("-" * 30)
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])
            print("-" * 30)

            found = True
            break

    if not found:
        print("Contact not found.\n")

def update_contact():
    print("\n Update Contact ")
    name = input("Enter Contact Name to Update: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            print("\nEnter New Details")

            contact["name"] = input("New Name: ")
            contact["phone"] = input("New Phone Number: ")
            contact["email"] = input("New Email: ")
            contact["address"] = input("New Address: ")

            print("\n Contact Updated Successfully!\n")
            found = True
            break

    if not found:
        print("Contact not found.\n")

def delete_contact():
    print("\n Delete Contact ")
    name = input("Enter Contact Name to Delete: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("\n Contact Deleted Successfully!\n")
            found = True
            break

    if not found:
        print("Contact not found.\n")

while True:

    print("\n" + "=" * 40)
    print("         CONTACT BOOK")
    print("=" * 40)

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank you for using Contact Book!")
        break

    else:
        print("\n Invalid Choice! Please enter a number between 1 and 6.")
