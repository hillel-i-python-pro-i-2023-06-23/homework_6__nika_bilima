import pathlib
from typing import Final

ROOT_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
FILES_INPUT_DIR: Final[pathlib.Path] = ROOT_DIR.joinpath("files_input")
