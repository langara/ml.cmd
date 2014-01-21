import ez_setup
ez_setup.use_setuptools()
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
    keywords = "vim launch command shell custom ipython qtile",
    url = "https://github.com/langara",
    entry_points = {
        'console_scripts': [
            'run = ml.cmd:main',
            'r = ml.cmd:main',
            'shell = ml.cmd:main',
            's = ml.cmd:main',
            'term = ml.cmd:main',
            't = ml.cmd:main',
            'edit = ml.cmd:main',
            'e = ml.cmd:main',
            'fmgr = ml.cmd:main',
            'f = ml.cmd:main',
        ]
    }
)

