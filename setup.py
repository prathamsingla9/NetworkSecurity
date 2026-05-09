from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    # this function will return the list of requirements
    requirement_list: list[str] = []
    try:
        with open('requirements.txt','r') as file:
            # read lines from file
            lines = file.readlines()
            # process each line
            for line in lines:
                # strip whitespace and ignore empty lines
                requirement = line.strip()
                # ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

# print(get_requirements())

setup(
    name = 'network_security',
    version = '0.0.1',
    author = 'Pratham Singla',
    author_email = 'singlapratham619@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
)