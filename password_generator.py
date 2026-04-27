import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+[]{}?"

    if not chars:
        return None

    return "".join(random.choice(chars) for _ in range(length))


def ask_yes_no(question):
    while True:
        ans = input(question + " (y/n): ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("  just type y or n.\n")


def main():
    print("\n  === password generator ===\n")

    # get length
    while True:
        raw = input("  how long should the password be? (8–64): ").strip()
        if raw.isdigit() and 8 <= int(raw) <= 64:
            length = int(raw)
            break
        print("  pick a number between 8 and 64.\n")

    print()

    # complexity options
    use_upper   = ask_yes_no("  include uppercase letters (A-Z)?")
    use_digits  = ask_yes_no("  include numbers (0-9)?")
    use_symbols = ask_yes_no("  include symbols (!@#$...)?")

    print()

    # generate and show
    password = generate_password(length, use_upper, use_digits, use_symbols)
    print("  your password:")
    print(f"\n    {password}\n")

    # offer to regenerate
    while True:
        again = input("  generate another with the same settings? (y/n): ").strip().lower()
        if again == "y":
            password = generate_password(length, use_upper, use_digits, use_symbols)
            print(f"\n    {password}\n")
        elif again == "n":
            print("\n  done. keep it safe!\n")
            break
        else:
            print("  y or n please.\n")


main()
