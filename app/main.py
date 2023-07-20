from app.services.reading_the_file import reading_the_file
from app.services.generate_users import generate_users, print_users
from app.services.who_is_there import get_astronaut_count, print_count
from app.services.average import calculate_average, print_average


def main():
    print("Mini-task 1:'Reading the file'")
    reading_the_file()

    print("\n\nMini-task 2:'Generate_users'")
    users = generate_users(50)
    print_users(users)

    print("\n\nMini-task 3:'Who is there?'")
    count = get_astronaut_count()
    print_count(count)

    print("\n\nMini-task 4:'Average'")
    average_h, average_w = calculate_average()
    print_average(average_h, average_w)
