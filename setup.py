from setuptools import setup, find_packages


setup(
    name='blockdiag-fences',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/oliversalzburg/markdown-blockdiag',
    license='MIT',
    install_requires=[
        'Markdown',
        'blockdiag',
        'seqdiag',
        'actdiag',
        'nwdiag',
    ],
    author='Oliver Salzburg',
    author_email='oliver.salzburg@gmail.com',
    description='blockdiag extension for Python Markdown'
)
