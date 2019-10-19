import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Online-Shop",
    version="0.0.1",
    author="Srikant",
    author_email="kumar_srikant@outlook.com",
    description="E-Commerce Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SRICKKY/Online-Shop.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
