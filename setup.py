try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup

config = {
	'discription': 'Game of Trade. The game is over when loses all the money and is won if earns to million dollar',
	'author': 'Anke Ge',
	'url':'URL',
	'download_url':'download_url',
	'author_email':'email',
	'version':'0.1',
	'install_requires':['flask'],
	'packages':find_packages(),
	'scripts':[],
	'name': 'trade to million'
	}

setup(**config)

