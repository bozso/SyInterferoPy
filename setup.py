from setuptools import setup, find_namespace_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="SyInterferoPy",
    version="0.1.0",
    # url='https://github.com/mypackage.git',
    # description='Description of my package',
    # packages=find_packages(where="pygeo", include="**"),
    packages=find_namespace_packages(
        include="syinterferopy.*",
        exclude=("SRTM3*", "build*", "readme_figures*", "dist*"),
    ),
    install_requires=requirements,
)
