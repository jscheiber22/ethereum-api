from setuptools import setup, find_packages

setup(
    name='ethereum-api',
    version='0.1.2',
    license='MIT',
    description='A library to more easily work with the Ethermine pool network API.',
    author='James Scheiber',
    author_email='jscheiber22@gmail.com',
    url="https://github.com/jscheiber22/ethereum-api",
    packages=find_packages(include=['ethereum', 'ethereum.*'])
)
