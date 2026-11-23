"""Smart Contact Book & Network Finder.

A console application demonstrating core Python concepts:
- Dictionaries: Contact storage and nested details (CRUD operations)
- Sets: Tag-based classification, mutual interests, and set operations (union, intersection, difference)
- Lists: Result aggregation and menu option displays
- Tuples: Immutable summary records for quick display
- Strings: Input sanitation (.strip(), .lower(), .title()), formatting, and validation
- Functions: Modular, reusable code blocks with parameters and return values
- Loops & Conditionals: While loops, for-enumerate loops, and if-elif-else logic
"""

# Initial contact database stored as a dictionary of dictionaries.
# Key: Contact Name (Title Case)
# Value: Dictionary containing phone, email, city, and a set of tags
contacts = {
    "Drupad S": {
        "phone": "+919876543210",
        "email": "drupads1522@gmail.com",
        "city": "Mysore",
        "tags": {"python", "developer", "colleague", "ai"}
    },
    "Ravi Kumar": {
        "phone": "+919123456780",
        "email": "ravi.kumar@example.com",
        "city": "Bangalore",
        "tags": {"python", "data", "college"}
    },
    "Ananya Sharma": {
        "phone": "+919845012345",
        "email": "ananya.s@example.com",
        "city": "Mysore",
        "tags": {"design", "colleague", "ui"}
    },
    "Karthik Rao": {
        "phone": "+919731234567",
        "email": "karthik.rao@example.com",
        "city": "Bangalore",
        "tags": {"college", "developer", "gaming"}
    }
}


def display_header(title):
    """Utility function to print styled section headers."""
    print("\n" + "=" * 55)
    print(f" {title} ".center(55, "-"))
    print("=" * 55)


def add_or_update_contact():
    """Add a new contact or update an existing contact's details."""
    display_header("ADD / UPDATE CONTACT")
    
    # String manipulation: strip leading/trailing spaces and format as Title Case
    name = input("Enter contact name: ").strip().title()
    if not name:
        print("[!] Contact name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip().lower()
    city = input("Enter city: ").strip().title()

    # Taking comma-separated tags and converting them to a Set of lowercase strings
    raw_tags = input("Enter tags separated by commas (e.g., python, work, college): ")
    # List comprehension to clean each tag, then converted to a set for unique tags
    tags_set = {tag.strip().lower() for tag in raw_tags.split(",") if tag.strip()}

    is_update = name in contacts
    contacts[name] = {
        "phone": phone,
        "email": email,
        "city": city,
        "tags": tags_set
    }

    status = "updated" if is_update else "added"
    print(f"[✓] Contact '{name}' successfully {status}!")


def view_all_contacts():
    """Display all contacts in a formatted overview."""
    display_header("ALL CONTACTS")
    if not contacts:
        print("No contacts found.")
        return

    # Using enumerate() to display index along with items
    for idx, (name, info) in enumerate(contacts.items(), start=1):
        # Convert tags set to a sorted list for neat, predictable printing
        tags_str = ", ".join(sorted(info["tags"])) if info["tags"] else "None"
        print(f"\n{idx}. {name}")
        print(f"   Phone : {info['phone']}")
        print(f"   Email : {info['email']}")
        print(f"   City  : {info['city']}")
        print(f"   Tags  : [{tags_str}]")


def search_by_name():
    """Search for contacts by partial name match."""
    display_header("SEARCH BY NAME")
    query = input("Enter name to search: ").strip().lower()

    if not query:
        print("[!] Search query cannot be empty.")
        return

    # Using a list to collect matching contact tuples: (name, phone, email)
    matches = []
    for name, details in contacts.items():
        if query in name.lower():
            matches.append((name, details["phone"], details["email"]))

    if matches:
        print(f"\nFound {len(matches)} match(es):")
        for name, phone, email in matches:
            print(f"- {name.ljust(20)} | Phone: {phone.ljust(15)} | Email: {email}")
    else:
        print(f"No contacts matching '{query}'.")


def search_by_tags():
    """Find contacts matching tags using Set operations."""
    display_header("SEARCH BY TAGS (SET OPERATIONS)")
    print("1. Match ALL tags (Intersection / Strict filter)")
    print("2. Match ANY tag  (Union / Broad filter)")
    choice = input("Select mode (1 or 2): ").strip()

    if choice not in ("1", "2"):
        print("[!] Invalid option selected.")
        return

    raw_query = input("Enter tag(s) separated by commas: ")
    query_tags = {tag.strip().lower() for tag in raw_query.split(",") if tag.strip()}

    if not query_tags:
        print("[!] Please enter at least one tag.")
        return

    matched_contacts = []
    for name, details in contacts.items():
        contact_tags = details["tags"]
        if choice == "1":
            # Set subset / intersection: contact must have ALL queried tags
            if query_tags.issubset(contact_tags):
                matched_contacts.append((name, contact_tags))
        elif choice == "2":
            # Set intersection: at least one tag is shared
            if bool(contact_tags & query_tags):
                matched_contacts.append((name, contact_tags))

    mode_label = "ALL" if choice == "1" else "ANY OF"
    print(f"\nContacts matching {mode_label} {query_tags}:")
    if matched_contacts:
        for name, tags in matched_contacts:
            print(f"- {name.ljust(20)} (Tags: {', '.join(sorted(tags))})")
    else:
        print("No contacts found matching the given tag criteria.")


def network_analysis():
    """Demonstrate advanced Set operations between contacts and group statistics."""
    display_header("NETWORK INSIGHTS & SET OPERATIONS")

    if len(contacts) < 2:
        print("[!] Need at least 2 contacts for comparison.")
        return

    # 1. Union across all contact tags to find all unique skills/interests in your network
    all_tags = set()
    all_cities = set()
    for details in contacts.values():
        all_tags = all_tags.union(details["tags"])  # or all_tags |= details["tags"]
        all_cities.add(details["city"])

    print(f"Total Unique Tags in Network ({len(all_tags)}): {', '.join(sorted(all_tags))}")
    print(f"Cities Covered ({len(all_cities)}): {', '.join(sorted(all_cities))}")

    # 2. Compare mutual connections between two specific contacts
    print("\n--- Compare Two Contacts ---")
    contact_names = list(contacts.keys())
    for idx, cname in enumerate(contact_names, start=1):
        print(f"  {idx}. {cname}")

    try:
        idx1 = int(input("\nSelect first contact number: ")) - 1
        idx2 = int(input("Select second contact number: ")) - 1

        if not (0 <= idx1 < len(contact_names) and 0 <= idx2 < len(contact_names)):
            print("[!] Invalid selection.")
            return

        name1 = contact_names[idx1]
        name2 = contact_names[idx2]

        tags1 = contacts[name1]["tags"]
        tags2 = contacts[name2]["tags"]

        # Set Intersection: Common interests / tags
        common_tags = tags1.intersection(tags2)  # or tags1 & tags2
        
        # Set Difference: Tags unique to each
        only_in_1 = tags1.difference(tags2)      # or tags1 - tags2
        only_in_2 = tags2.difference(tags1)      # or tags2 - tags1

        # Symmetric Difference: Tags that either has, but not both
        sym_diff = tags1.symmetric_difference(tags2)  # or tags1 ^ tags2

        print(f"\nComparing '{name1}' and '{name2}':")
        print(f"• Common tags (Intersection): {common_tags if common_tags else 'None'}")
        print(f"• Tags unique to {name1} (Difference): {only_in_1 if only_in_1 else 'None'}")
        print(f"• Tags unique to {name2} (Difference): {only_in_2 if only_in_2 else 'None'}")
        print(f"• Tags in either but not both (Symmetric Difference): {sym_diff if sym_diff else 'None'}")

    except ValueError:
        print("[!] Please enter valid numbers.")


def delete_contact():
    """Delete a contact using dictionary deletion."""
    display_header("DELETE CONTACT")
    name = input("Enter exact contact name to delete: ").strip().title()

    # del / pop from dictionary
    if name in contacts:
        removed = contacts.pop(name)
        print(f"[✓] Deleted contact '{name}' (Phone: {removed['phone']}).")
    else:
        print(f"[!] Contact '{name}' not found.")


def main():
    """Main program loop with interactive CLI menu."""
    while True:
        display_header("SMART CONTACT BOOK & NETWORK FINDER")
        print("1. View All Contacts")
        print("2. Add / Update Contact")
        print("3. Search Contact by Name")
        print("4. Search Contacts by Tags (Set Filter)")
        print("5. Network Insights & Set Comparisons")
        print("6. Delete Contact")
        print("7. Exit")
        print("=" * 55)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            view_all_contacts()
        elif choice == "2":
            add_or_update_contact()
        elif choice == "3":
            search_by_name()
        elif choice == "4":
            search_by_tags()
        elif choice == "5":
            network_analysis()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            print("\nThank you for using Smart Contact Book. Goodbye!")
            break
        else:
            print("\n[!] Invalid option. Please enter a number between 1 and 7.")

        input("\nPress Enter to return to main menu...")


if __name__ == "__main__":
    main()
