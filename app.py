from flask import Flask, Response

from webargs import fields
from webargs.flaskparser import use_args

from app.services.generate_users import generate_users
from app.services.who_is_there import get_astronaut_count
from app.services.average import calculate_average
from app.services.reading_the_file import reading_the_file

from app.services.create_table import create_table

from app.services.db_connection import DBConnection

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


@app.route("/users/create")
@use_args({"name": fields.Str(required=True), "phone": fields.Str(required=True)}, location="query")
def users_create(args):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "INSERT INTO users (contact_name, phone_value) VALUES (:name, :phone);",
                {"name": args["name"], "phone": args["phone"]},
            )

        return "Successfully"


@app.route("/users/read-all")
def users_read_all():
    with DBConnection() as connection:
        users = connection.execute("SELECT * FROM users;").fetchall()

    return "<br>".join([f'{user["pk"]}    <b>{user["contact_name"]}</b>: {user["phone_value"]}' for user in users])


@app.route("/users/read/<int:pk>")
def users_read(pk: int):
    with DBConnection() as connection:
        user = connection.execute(
            "SELECT * " "FROM users " "WHERE (pk=:pk);",
            {
                "pk": pk,
            },
        ).fetchone()

    return f"{user['pk']}:    <b>{user['contact_name']}</b>: {user['phone_value']}"


@app.route("/users/update/<int:pk>")
@use_args({"name": fields.Str(), "phone": fields.Str()}, location="query")
def users_update(
    args,
    pk: int,
):
    with DBConnection() as connection:
        with connection:
            name = args.get("name")
            phone = args.get("phone")

            if name is None and phone is None:
                return Response(
                    "Need to provide at least one argument",
                    status=404,
                )

            args_for_request = []
            if name is not None:
                args_for_request.append("contact_name=:name")
            if phone is not None:
                args_for_request.append("phone_value=:phone")

            args_2 = ", ".join(args_for_request)

            connection.execute(
                "UPDATE users " f"SET {args_2} " "WHERE pk=:pk;",
                {
                    "pk": pk,
                    "name": name,
                    "phone": phone,
                },
            )
    return "Successfully"


@app.route("/users/delete/<int:pk>")
def users_delete(pk):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "DELETE " "FROM users " "WHERE (pk=:pk);",
                {
                    "pk": pk,
                },
            )
    return "Successfully"


create_table()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
