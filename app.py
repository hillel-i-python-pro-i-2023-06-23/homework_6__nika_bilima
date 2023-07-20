from app.services.generate_users import generate_users
from app.services.who_is_there import get_astronaut_count
from app.services.average import calculate_average
from flask import Flask
from app.services.reading_the_file import reading_the_file

app = Flask(__name__)


@app.route("/")
def info():
    data = "Enter the name of func you want to illustrate."
    return data


@app.route("/get-content/")
def read_the_file():
    content = reading_the_file()
    return content


@app.route("/generate-users/")
@app.route("/generate-users/<int:num_of_users>")
def get_users(num_of_users=100):
    generated_users = generate_users(num_of_users)
    users_list = list(generated_users)
    return "<br>".join(users_list)


@app.route("/space/")
def astronauts():
    count = get_astronaut_count()
    return f"There are currently <b>{count}</b> astronauts on the ISS."


@app.route("/mean/")
def average():
    height, weight = calculate_average()
    return f"Average height: <b>{height}</b> cm<br>Average weight: <b>{weight}</b> kg"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
