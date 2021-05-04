from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements

print(read_requirements())

setup(
    name="noob",
    version="0.1",
    py_modules=['ed'],
    packages=find_packages(),
    include_package_data =True,
    install_requires=read_requirements(),
    entry_points='''
        [console_scripts]
        ed=ed.cli:cli
    '''
)