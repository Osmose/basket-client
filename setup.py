from setuptools import setup, find_packages


setup(
    name='basket',
    version='0.1.0',
    description='A thin, practical wrapper around terminal formatting, positioning, and more',
    long_description=open('README.rst').read(),
    author='Erik Rose',
    author_email='erikrose@grinchcentral.com',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    tests_require=['Nose'],
    url='https://github.com/erikrose/blessings',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals'
        ],
    keywords=['terminal', 'tty', 'curses', 'formatting', 'color'],
    **extra_setup
)
