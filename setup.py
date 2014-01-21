from setuptools import setup, find_packages
setup(
    name = 'ml.cmd',
    version = '0.2',
    packages = find_packages(),
    install_requires = ['docopt>=0.6.1'],
    author = "Marek Langiewicz",
    author_email = "marek.langiewicz@gmail.com"
    description = "Collection of custom shortcut commands to use either as shell commands or as python functions.",
    licence = "MIT",
    keywords = "vim launch command shell custom",
    url = "https://github.com/langara"

)

