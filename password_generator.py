
import secrets
import string

# Liste des mots de passe générés (stockage en mémoire)
passwords = []


def generate_password(length=12, use_special=True, use_numbers=True):
    if length < 6:
        raise ValueError(
            "La longueur du mot de passe doit être au moins de 6 caractères."
        )

    # Caractères disponibles
    chars = string.ascii_lowercase  # Lettres minuscules uniquement par défaut
    password = []

    # Ajout d'un caractère obligatoire pour chaque catégorie activée
    if use_numbers:
        chars += string.digits
        password.append(secrets.choice(string.digits))  # Ajoute un chiffre
    if use_special:
        chars += string.punctuation
        password.append(
            secrets.choice(string.punctuation)
        )  # Ajoute un caractère spécial

    # Ajout d'au moins une lettre majuscule
    chars += string.ascii_uppercase
    password.append(secrets.choice(string.ascii_uppercase))  # Ajoute une majuscule

    # Compléter le mot de passe pour atteindre la longueur spécifiée
    password += [secrets.choice(chars) for _ in range(length - len(password))]

    # Mélanger de manière sécurisée
    secrets.SystemRandom().shuffle(password)

    password = "".join(password)
    passwords.append(password)
    return password


def show_passwords():
    """Afficher tous les mots de passe générés."""
    if not passwords:
        return "Aucun mot de passe généré pour l'instant."
    return "\n".join(f"{i + 1}. {pw}" for i, pw in enumerate(passwords))


def check_password_strength(password):
    """Évaluer la force d'un mot de passe."""
    strength = 0

    # Check length (8 or more)
    if len(password) >= 8:
        strength += 1

    # Check for at least one uppercase letter
    if any(c.isupper() for c in password):
        strength += 1

    # Check for at least one digit
    if any(c.isdigit() for c in password):
        strength += 1

    # Check for at least one special character
    if any(c in string.punctuation for c in password):
        strength += 1

    # If the password has at least length 8 and no other strength factors, classify as "Moyenne"
    if strength == 1:
        return "Moyenne"

    # Adjust strength based on the criteria
    if strength == 2:
        return "Moyenne"
    elif strength == 3:
        return "Forte"
    elif strength == 4:
        return "Très Forte"

    return "Faible"  # Default case


def save_passwords_to_file(filename="passwords.txt"):
    """Sauvegarder les mots de passe dans un fichier."""
    if not passwords:
        return "Aucun mot de passe à sauvegarder."  # Check for empty list
    with open(filename, "w") as f:
        for i, pw in enumerate(passwords):
            f.write(f"{i + 1}. {pw}\n")
    return f"Les mots de passe ont été sauvegardés dans le fichier {filename}"


def retrieve_password(index):
    """Récupérer un mot de passe par index."""
    if index < 1 or index > len(passwords):
        raise IndexError("Index hors limite")
    return passwords[index - 1]


def main():
    print("Bienvenue dans le générateur de mots de passe sécurisé !")
    while True:
        print("\nOptions :")
        print("1. Générer un nouveau mot de passe")
        print("2. Afficher les mots de passe générés")
        print("3. Vérifier la force d'un mot de passe")
        print("4. Sauvegarder les mots de passe dans un fichier")
        print("5. Récupérer un mot de passe")
        print("6. Quitter")
        choice = input("Choisissez une option : ").strip()

        if choice == "1":
            try:
                length = int(input("Entrez la longueur du mot de passe (min 6) : "))
                use_special = (
                    input("Inclure des caractères spéciaux ? (oui/non) : ")
                    .strip()
                    .lower()
                    == "oui"
                )
                use_numbers = (
                    input("Inclure des chiffres ? (oui/non) : ").strip().lower()
                    == "oui"
                )
                password = generate_password(length, use_special, use_numbers)
                print(f"Mot de passe généré : {password}")
            except ValueError as e:
                print(f"Erreur : {e}")
        elif choice == "2":
            print("\nMots de passe générés :")
            print(show_passwords())
        elif choice == "3":
            password = input("Entrez le mot de passe à vérifier : ").strip()
            print(f"Force du mot de passe : {check_password_strength(password)}")
        elif choice == "4":
            filename = (
                input(
                    "Entrez le nom du fichier de sauvegarde (par défaut: passwords.txt) : "
                ).strip()
                or "passwords.txt"
            )
            print(save_passwords_to_file(filename))
        elif choice == "5":
            try:
                index = int(input("Entrez le numéro du mot de passe à récupérer : "))
                print(f"Mot de passe récupéré : {retrieve_password(index)}")
            except (ValueError, IndexError) as e:
                print(f"Erreur : {e}")
        elif choice == "6":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
