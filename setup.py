from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dante-corpora',
    version='2.0.0',
    description='Pacote Python contendo os corpora do projeto DANTE do POeTiSA',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='felmateos',
    author_email='felmateos@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'dante': ['data/**/*']
    },
    install_requires=[
        'pandas==2.2.2'
    ],
    license='MIT'
)