from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dante-corpora',
    version='1.0.6',
    description='Pacote Python contendo os corpora do projeto DANTE do POeTiSA',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='felmateos',
    author_email='felmateos@gmail.com',
    packages=find_packages(),
    package_data={
        'dante': ['data/danteshots.csv', 'data/dantestocks.csv']
    },
    install_requires=[
        'pandas==2.2.2'
    ],
    license='MIT'
)
