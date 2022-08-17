from setuptools import setup, find_packages
import re

VERSIONFILE="msldap/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


setup(
	# Application name:
	name="msldap",

	# Version number (initial):
	version=verstr,

	# Application author details:
	author="Tamas Jos",
	author_email="info@skelsecprojects.com",

	# Packages
	packages=find_packages(),

	# Include additional files into the package
	include_package_data=True,


	# Details
	url="https://github.com/skelsec/msldap",

	zip_safe = False,
	#
	# license="LICENSE.txt",
	description="Python library to play with MS LDAP",
	long_description="Python library to play with MS LDAP",

	# long_description=open("README.txt").read(),
	python_requires='>=3.7',
	classifiers=(
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
	install_requires=[
		'asn1crypto>=1.3.0',
		'unicrypto>=0.0.5',
		'uniauth>=0.0.1',
		'aysocks>=0.2.0',
		'minikerberos>=0.3.0',
		'winacl>=0.1.2',
		'prompt-toolkit>=3.0.2',
		'tqdm',
		'wcwidth',
	],
	entry_points={
		'console_scripts': [
			'msldap = msldap.examples.msldapclient:main',
			'msldapcompdns = msldap.examples.msldapcompdnslist:main',
		],
	}
)