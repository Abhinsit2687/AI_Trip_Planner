from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements

    """
    requirement_list:List[str] = []

    try:
        # ope and read the requirements.txxt file
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process 
            for line in lines:
                # Strip whitespaces and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

print(get_requirements())


setup(
    name = "AI-TRAVEL-PLANNER",
    version = "0.0.1",
    author = "abhishek_gupta",
    author_email="gupta.abhi2687@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements()
)






