import pytest
from username_generator import generate_username, show_usernames, save_usernames_to_file, usernames

@pytest.fixture(autouse=True)
def reset_usernames():
    usernames.clear()

def test_generate_username_default():
    username = generate_username()
    assert len(username) == 8
    assert username.isalnum()

def test_generate_username_custom_length():
    username = generate_username(12)
    assert len(username) == 12

def test_generate_username_min_length():
    with pytest.raises(ValueError):
        generate_username(2)

def test_show_usernames_empty():
    assert show_usernames() == "No usernames generated yet."

def test_show_usernames_non_empty():
    generate_username()
    assert "1." in show_usernames()
    generate_username()
    assert "2." in show_usernames()

def test_save_usernames_to_file(tmp_path):
    usernames.extend(["user1", "user2"])
    file = tmp_path / "usernames.txt"
    message = save_usernames_to_file(file)
    assert file.exists()
    assert "Usernames saved to" in message
    with open(file) as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0].strip() == "1. user1"
        assert lines[1].strip() == "2. user2"

def test_save_usernames_to_file_empty(tmp_path):
    file = tmp_path / "empty_usernames.txt"
    message = save_usernames_to_file(file)
    assert "No usernames to save." in message
    assert not file.exists()
