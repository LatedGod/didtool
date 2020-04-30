import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="didtool",
    version="0.0.1",
    author="dustless",
    author_email="wuchenghui927@126.com",
    description="Tool set for feature engineering & modeling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dustless/didtool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
