from pathlib import Path


def root_path(file_name):
    return str(Path(__file__).parent.parent.joinpath(file_name).absolute())