"""generate setup.json from Pipfile"""

from hass_py.utils import DependencyParser

print("reading Pipfile")
dp = DependencyParser("Pipfile")

print("dumping setup.json")
dp.dump_requirements("setup.json")

print("done")
