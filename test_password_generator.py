import pytest
from password_generator import (
    generate_password,
    show_passwords,
    check_password_strength,
    save_passwords_to_file,
    retrieve_password,
    passwords,
)
import string


@pytest.fixture(autouse=True)
def reset_passwords():
    passwords.clear()


def test_generate_password_default():
    password = generate_password()
    assert len(password) == 12
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in string.punctuation for c in password)


def test_generate_password_no_special():
    password = generate_password(use_special=False)
    assert len(password) == 12
    assert all(c not in string.punctuation for c in password)


def test_generate_password_no_numbers():
    password = generate_password(use_numbers=False)
    assert len(password) == 12
    assert all(c not in string.digits for c in password)


def test_generate_password_min_length():
    with pytest.raises(ValueError):
        generate_password(length=5)


def test_generate_password_with_large_length():
    password = generate_password(length=100)
    assert len(password) == 100


def test_check_password_strength():
    assert check_password_strength("") == "Faible"
    assert check_password_strength("12345678") == "Moyenne"
    assert check_password_strength("abcdefgh") == "Moyenne"  # Fixed logic
    assert check_password_strength("Abcd1234") == "Forte"
    assert check_password_strength("Abcd1234!") == "Très Forte"


def test_show_passwords_empty():
    assert show_passwords() == "Aucun mot de passe généré pour l'instant."


def test_show_passwords_non_empty():
    generate_password()
    assert "1." in show_passwords()
    generate_password()
    assert "2." in show_passwords()


def test_save_passwords_to_file(tmp_path):
    passwords.extend(["pass1", "pass2"])
    file = tmp_path / "passwords.txt"
    message = save_passwords_to_file(file)
    assert file.exists()
    assert "Les mots de passe ont été sauvegardés" in message
    with open(file) as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0].strip() == "1. pass1"
        assert lines[1].strip() == "2. pass2"


def test_save_passwords_to_file_empty(tmp_path):
    file = tmp_path / "passwords_empty.txt"
    message = save_passwords_to_file(file)
    assert "Aucun mot de passe à sauvegarder." in message  # Fixed behavior
    assert not file.exists()


def test_retrieve_password():
    passwords.extend(["pass1", "pass2"])
    assert retrieve_password(1) == "pass1"
    assert retrieve_password(2) == "pass2"
    with pytest.raises(IndexError):
        retrieve_password(3)
    with pytest.raises(IndexError):
        retrieve_password(0)