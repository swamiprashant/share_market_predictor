from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]



    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)  

    return requirements

setup(
    name = "share market predictor",
    version = "0.0.1",
    auther = "swamiprashant",
    author_email="swamiprashantsanjay@gmail.com",
    requirements=get_requirements("requirements.txt"),
    packeges=find_packages()
)