from setuptools import setup, find_packages


PKG_NAME = 'sanitize'

setup(
    name=PKG_NAME,
    version=".".join(map(str, __import__(PKG_NAME).__version__)),
    description="Bringing sanitiy to world of messed-up data",
    long_description=open('README.md').read(),
    author="Aaron Swartz",
    author_email="me@aaronsw.com",
    maintainer='Alireza Savand',
    maintainer_email='alireza.savand@gmail.com',
    url='http://www.aaronsw.com/2002/sanitize/',
    license=open('LICENCE').read(),
    packages=find_packages(),
    py_modules=[PKG_NAME],
    include_package_data=True,
    zip_safe=False,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
