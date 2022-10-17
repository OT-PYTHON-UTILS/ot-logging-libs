from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='otlogginglibs',
    version='1.0.0',
    description='Python logging library',
    author='Himanshi Parnami',
    author_email='himanshi.parnami@opstree.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["otlogginglibs"],
    python_requires=">=3.6",
)