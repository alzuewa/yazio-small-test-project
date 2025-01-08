from pathlib import Path

import tests


def get_path_from_root(relative_path: str):
    return Path(tests.__file__).parent.parent.joinpath(relative_path).absolute().__str__()
