import sys

from setuptools import setup, find_packages

setup(
    name = "culturemap-multimedia",
    version = '12.05',
    description = "Alternative Armstrong CMS app for embedding multimedia into site.",
    url = "https://github.com/mouthwateringmedia/CultureMap-Multimedia",
    author = "Paul Bailey",
    author_email = "paul.m.bailey@gmail.com",
    license = "BSD",
    packages = [
      'cm_multimedia',
      'cm_multimedia.migrations',
    ],
    include_package_data = True,
)

