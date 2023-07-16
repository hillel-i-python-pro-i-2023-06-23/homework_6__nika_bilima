from app.services.reading_the_file import reading_the_file
from app.services.generate_users import generate_users, print_users


def main():
    reading_the_file()

    users = generate_users(50)
    print_users(users)
