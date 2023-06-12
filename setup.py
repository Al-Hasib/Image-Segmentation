from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    # returs a list of files
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')


setup(
    name = 'Image-Segmentation',
    version = '0.0.1',
    author = 'Abdullah',
    author_email = 'mdabdullahalhasib1111@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)