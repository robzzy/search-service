# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name="search",
    version="0.0.1",
    description="Use to manage search-service",
    packages=find_packages("src", exclude=["test"]),
    package_dir={"": "src"},
    install_requires=[
        "elasticsearch-dsl>=7.0.0,<8.0.0",
        "nameko==3.0.0-rc9",
        "nameko-tracer==1.2.0",
    ],
    extras_require={
        "dev": [
            "pytest==6.0.1",
            "coverage==4.5.3",
            "flake8>=3.7.7",
            "black==19.10b0",
        ]
    },
    zip_safe=True,
)
