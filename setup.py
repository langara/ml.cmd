import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(
    name = 'ml.cmd',
    version = '0.2.2',
    packages = find_packages(),
    install_requires = ['docopt>=0.6.1'],
    author = "Marek Langiewicz",
    author_email = "marek.langiewicz@gmail.com",
    description = "Collection of custom shortcut commands to use either as shell commands or as python functions.",
    license = "MIT",
    keywords = "vim launch command shell custom ipython qtile",
    url = "https://github.com/langara",
    entry_points = {
        'console_scripts': [
            'cmd = ml.cmd:main',
            'run = ml.cmd:main',
            'shell = ml.cmd:main',
            'term = ml.cmd:main',
            'edit = ml.cmd:main',
            'openf = ml.cmd:main',
            'lopenf = ml.cmd:main',
            'play = ml.cmd:main',
            'hist = ml.cmd:main',
            'decomp = ml.cmd:main',
            'diff = ml.cmd:main',
            'fmgr = ml.cmd:main',
            'fehback = ml.cmd:main',
            'usrcmd = ml.cmd:main',
            'r = ml.cmd:main',
            's = ml.cmd:main',
            't = ml.cmd:main',
            'e = ml.cmd:main',
            'o = ml.cmd:main',
            'lo = ml.cmd:main',
            'p = ml.cmd:main',
            'h = ml.cmd:main',
            'de = ml.cmd:main',
            'd = ml.cmd:main',
            'f = ml.cmd:main',
            'fb = ml.cmd:main',
            'uc = ml.cmd:main',
        ]
    },
    zip_safe = True,
    namespace_packages = ['ml']
)

