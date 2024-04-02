from distutils.core import setup

REQUIRES = [
    'allure-pytest',
    'records',
    'structlog'
]

setup(
    name='db_client',
    version='1.1.1',
    packages=['db_client'],
    url='https://github.com/katyakorsa/db_client.git',
    license='MIT',
    author='Ekaterina Korsakova',
    author_email='',
    install_requires=REQUIRES,
    description='data base client with logging and allure'
)
