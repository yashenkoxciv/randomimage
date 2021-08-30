from setuptools import setup


setup(
    name='randomimage',
    version='0.1',
    description='get random image from https://picsum.photos/',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yashenkoxciv/randomimage',
    author='Artem Yaschenko',
    author_email='yashenkoxciv@gmail.com',
    license='MIT',
    packages=['randomimage'],
    install_requires=open('requirements.txt', 'r').read().split('\n')
)