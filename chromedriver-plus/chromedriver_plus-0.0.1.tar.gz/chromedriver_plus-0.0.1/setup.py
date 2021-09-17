import setuptools

setuptools.setup(
    name="chromedriver_plus",
    version="0.0.1",
    author="Tat Nguyen Van",
    author_email="nguyenvantat7788@gmail.com",
    description="Some of my favorite features",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    packages=setuptools.find_packages(where='src'),
    python_requires=">=3.7",
    install_requires=[
        "undetected-chromedriver",
    ],
)