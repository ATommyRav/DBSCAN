from setuptools import setup, find_packages

setup(
    name="Projet_dbscan",
    version="1.0.0",
    author="Tommmy&Mahaliana",
    description="Projet DBSCAN sans scikit-learn",
    packages=find_packages(),
    install_requires=["numpy"],
    python_requires=">=3.6",
)
