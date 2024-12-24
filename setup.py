
## Package Manager will install the package by using the setup.py or pyproject.toml so no need to install the requirements.txt file, instead will use setup.py to install packages
## This is possible as we used -e . in the requirements.txt file

import setuptools 

with open("README.md" , "r" , encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "END-TO-END-TEXT-SUMMARIZER"
AUTHOR_USER_NAME = "PreetKumarPanchani"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL= "preetpanchani1@gmail.com"


setuptools.setup(
    name= SRC_REPO,
    version=__version__ ,
    author= AUTHOR_USER_NAME ,
    author_email= AUTHOR_EMAIL ,
    description="A small python package for summarizing text using Transformers" , 
    long_description = long_description ,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}" ,
    project_urls= {
        "Bug_Trackers" : "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues" , 

    },
    package_dir= {"": "src"},
    packages=setuptools.find_packages(where= "src") ,


)

