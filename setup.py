from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def readme():
    with open('README.md') as readme_file:
        return readme_file.read()


setup(
    name='clock',
    version='0.0.0',
    description='Datetime setup useful for IoC usage. Inspired by Dart-quiver\'s Clock.',
    long_description=readme(),
    keywords='system clock datetime time',
    url='http://github.com/horia141/silver',
    author='Horia Coman',
    author_email='horia141@gmail.com',
    license='All right reserved',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=[
        'pytz==2015.7',
        # For testing
        'coverage==4.1b1',
        'tabletest==1.1.0',
        ],
    test_suite='tests',
    tests_require=[],
    include_package_data=True,
    zip_safe=False
)
