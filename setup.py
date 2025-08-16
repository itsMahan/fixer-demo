from setuptools import setup


setup(
    name='fixer-demo',
    version='0.2',
    description='Fixer service Demo package',
    url='https://github.com/itsMahan/fixer-demo.git', #github repo
    author='Mahan',
    author_email='ataeifarmahan@gmail.com',
    license='MIT',
    packages=['fixer'],
    install_requires=['requests'],
    zip_safe=False,
)