import secrets
import string

# Storage for generated usernames
usernames = []

def generate_username(length=8):
    if length < 3:
        raise ValueError("The username length must be at least 3 characters.")

    # Character set: letters and digits
    chars = string.ascii_letters + string.digits
    username = ''.join(secrets.choice(chars) for _ in range(length))
    usernames.append(username)
    return username

def show_usernames():
    """Display all generated usernames."""
    if not usernames:
        return "No usernames generated yet."
    return "\n".join(f"{i + 1}. {username}" for i, username in enumerate(usernames))

def save_usernames_to_file(filename="usernames.txt"):
    """Save usernames to a file."""
    if not usernames:
        return "No usernames to save."
    with open(filename, "w") as file:
        for i, username in enumerate(usernames):
            file.write(f"{i + 1}. {username}\n")
    return f"Usernames saved to {filename}"

def main():
    print("Welcome to the Username Generator!")
    while True:
        print("\nOptions:")
        print("1. Generate a new username")
        print("2. Show generated usernames")
        print("3. Save usernames to a file")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                length = int(input("Enter username length (min 3): "))
                username = generate_username(length)
                print(f"Generated username: {username}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            print("\nGenerated Usernames:")
            print(show_usernames())
        elif choice == "3":
            filename = input("Enter filename (default: usernames.txt): ").strip() or "usernames.txt"
            print(save_usernames_to_file(filename))
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
