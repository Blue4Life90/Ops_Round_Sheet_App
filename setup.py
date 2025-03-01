from setuptools import setup, find_packages

setup(
    name="operator_rounds",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.20.0",
        "pandas>=1.3.0",
    ],
)