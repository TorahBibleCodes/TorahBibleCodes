import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='torahbiblecodes',
    version='1.0.3',
    author='torahbiblecodes',
    author_email='',
    description='An understandable multilanguaje and multithreading bible codes . Study the Torah as never before Bible Codes python library . An understandable multilanguaje and multithreading bible codes . Study the Torah as never before',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    #packages=find_packages(exclude=['tests']),
    packages=['torahbiblecodes', 'torahbiblecodes/modules', 'torahbiblecodes/resources/func', 'torahbiblecodes/resources/data'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='torahbiblecodes',
    python_requires='>=3.6.0',
    install_requires=[
        'configparser',
        'lxml',
        'python-hebrew-numbers',
        'textblob',
        'deep_translator'
    ],
    entry_points={
        'console_scripts': [
            'tbc-cli=torahbiblecodes.TBC:main'
        ],
    },
    project_urls={
        'Source': 'https://github.com/pedroelbanquero/TorahBibleCodes',
    },
)
