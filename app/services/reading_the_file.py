from app.config import FILES_INPUT_DIR


def reading_the_file():
    text_file = FILES_INPUT_DIR.joinpath("text_for_func_reading_the_file.txt")
    with open(text_file) as file:
        print(file.read())
