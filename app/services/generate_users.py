from faker import Faker


def generate_users(num_of_users = 100):
    fake = Faker()
    for _ in range(num_of_users):
        name = fake.first_name()
        email = fake.email()

        yield f"№{_+1}: {name}    {email}"


def print_users(generated_users):
    for user in generated_users:
        print(user)
