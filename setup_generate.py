"""generate setup.json from Pipfile"""

from pathlib import Path

from hass_py.utils import DependencyParser

print("reading Pipfile")
dp = DependencyParser(Path("Pipfile"))

print("dumping setup.json")
dp.dump_requirements(Path("setup.json"))

print("done")
