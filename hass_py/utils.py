# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_utils.ipynb.

# %% auto 0
__all__ = ['DependencyParser']

# %% ../nbs/00_utils.ipynb 5
import toml


class DependencyParser:
    """parse a pipfile to get the requirements

    Parameters
    ----------
    path_to_pipfile : str
        path to the pipfile

    """

    def __init__(self, path_to_pipfile: str):
        self.path_to_pipfile = path_to_pipfile
        with open(path_to_pipfile) as f:
            self.pipfile = toml.load(f)

    def __repr__(self):
        return f"DependencyParser({self.path_to_pipfile})"

    @staticmethod
    def pipenv_to_setuptools(package_name: str, contraints: str | dict) -> str:
        if contraints == "*":
            res = f"{package_name}"
        elif (contraints != "*") and isinstance(contraints, str):
            res = f"{package_name}{contraints}"
        elif isinstance(contraints, dict):
            res = f"{package_name}{contraints['version']}"

            # if extras := contraints.get("extras"):
            #     extras = [f"'{e}'" for e in extras]  # add ' to extras in list
            #     package_name = f"{package_name}[{','.join(extras)}]"
            #     res = f"{package_name}{contraints['version']}"
            # else:
            #     res = f"{package_name}{contraints['version']}"
        else:
            raise ValueError(f"Could not parse {package_name}, {contraints}")

        return res

    @property
    def min_python(self) -> str:
        return self.pipfile["requires"]["python_version"]

    @property
    def requirements(self):
        return [
            self.pipenv_to_setuptools(k, v) for k, v in self.pipfile["packages"].items()
        ]

    @property
    def dev_requirements(self):
        return [
            self.pipenv_to_setuptools(k, v)
            for k, v in self.pipfile["dev-packages"].items()
        ]

    def dump_requirements(self, path: str):
        import json

        with open(path, "w") as f:
            reqs = {
                "_comment": "# WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT!",
                "min_python": self.min_python,
                "requirements": self.requirements,
                "dev_requirements": self.dev_requirements,
            }
            json.dump(reqs, f, indent=4)
