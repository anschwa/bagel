from setuptools import setup


setup(
    name='bagel',
    packages=['bagel'],
    version='0.3.2',
    description='Bagel is a naive and language-agnostic static site generator',
    author='Adam Schwartz',
    author_email='adam@anschwa.com',
    url='https://github.com/anschwa/bagel',
    download_url='https://github.com/anschwa/bagel/tarball/0.3.2',
    entry_points={
        'console_scripts': [
            'bagel=bagel.bagel:main',
        ]
    },
    classifiers=[],
)
