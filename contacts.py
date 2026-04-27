import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


def print_contact(c, index=None):
    prefix = f"  {index}." if index is not None else "  "
    print(f"{prefix} {c['name']}  |  {c['phone']}")


def print_contact_full(c):
    print()
    print(f"  name:    {c['name']}")
    print(f"  phone:   {c['phone']}")
    print(f"  email:   {c['email']  or '—'}")
    print(f"  address: {c['address'] or '—'}")
    print()


def show_all(contacts):
    if not contacts:
        print("\n  no contacts yet. add one first.\n")
        return

    print(f"\n  contacts ({len(contacts)} total):")
    print("  " + "-" * 36)
    for i, c in enumerate(contacts, start=1):
        print_contact(c, i)
    print()


def ask(prompt, required=True):
    while True:
        val = input(f"  {prompt}: ").strip()
        if val:
            return val
        if not required:
            return ""
        print("  this one's required.\n")


def phone_exists(contacts, phone, skip_index=None):
    for i, c in enumerate(contacts):
        if i == skip_index:
            continue
        if c["phone"] == phone:
            return True
    return False


def pick_contact(contacts, prompt="  enter contact number: "):
    show_all(contacts)
    if not contacts:
        return None

    raw = input(prompt).strip()
    if not raw.isdigit() or not (1 <= int(raw) <= len(contacts)):
        print("\n  invalid number.\n")
        return None

    return int(raw) - 1   # return index


def add_contact(contacts):
    print("\n  -- add contact --")

    name = ask("name")

    while True:
        phone = ask("phone")
        if phone_exists(contacts, phone):
            print("  that number's already saved.\n")
        else:
            break

    email   = ask("email (optional)", required=False)
    address = ask("address (optional)", required=False)

    contacts.append({
        "name":    name,
        "phone":   phone,
        "email":   email,
        "address": address,
    })

    save_contacts(contacts)
    print(f"\n  saved: {name}\n")


def search_contact(contacts):
    if not contacts:
        print("\n  no contacts to search.\n")
        return

    print("\n  -- search --")
    query = ask("name or phone").lower()

    results = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]

    if not results:
        print(f"\n  nothing found for \"{query}\".\n")
        return

    print(f"\n  {len(results)} result(s):")
    print("  " + "-" * 36)
    for c in results:
        print_contact_full(c)


def view_contact(contacts):
    print("\n  -- view contact --")
    idx = pick_contact(contacts)
    if idx is None:
        return
    print_contact_full(contacts[idx])


def update_contact(contacts):
    print("\n  -- update contact --")
    idx = pick_contact(contacts)
    if idx is None:
        return

    c = contacts[idx]
    print(f"\n  editing: {c['name']}  (leave blank to keep current value)")
    print()

    name = input(f"  name [{c['name']}]: ").strip()
    if name:
        c["name"] = name

    while True:
        phone = input(f"  phone [{c['phone']}]: ").strip()
        if not phone:
            break
        if phone_exists(contacts, phone, skip_index=idx):
            print("  that number belongs to another contact.\n")
        else:
            c["phone"] = phone
            break

    email = input(f"  email [{c['email'] or '—'}]: ").strip()
    if email:
        c["email"] = email

    address = input(f"  address [{c['address'] or '—'}]: ").strip()
    if address:
        c["address"] = address

    save_contacts(contacts)
    print(f"\n  updated: {c['name']}\n")


def delete_contact(contacts):
    print("\n  -- delete contact --")
    idx = pick_contact(contacts)
    if idx is None:
        return

    name = contacts[idx]["name"]
    confirm = input(f"  delete \"{name}\"? (y/n): ").strip().lower()

    if confirm == "y":
        contacts.pop(idx)
        save_contacts(contacts)
        print(f"\n  deleted: {name}\n")
    else:
        print("\n  cancelled.\n")


def main():
    contacts = load_contacts()

    print("\n  === contact book ===")

    while True:
        print("  1. add contact")
        print("  2. view all contacts")
        print("  3. view a contact")
        print("  4. search")
        print("  5. update contact")
        print("  6. delete contact")
        print("  7. quit")

        choice = input("\n  > ").strip()
        print()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_all(contacts)
        elif choice == "3":
            view_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            update_contact(contacts)
        elif choice == "6":
            delete_contact(contacts)
        elif choice == "7":
            print("  bye.\n")
            break
        else:
            print("  pick a number from 1 to 7.\n")


main()