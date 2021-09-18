import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycobol2csv",
    packages=["pycobol2csv"],
    version="0.1.1",
    license="MIT",
    description="A Python library to convert COBOL ebcdic file to CSV format",
    author="Jason Li",
    author_email="niomobileapp@gmail.com",
    url="https://github.com/jasonli-lijie/pycobol2csv",
    download_url="https://github.com/user/reponame/archive/v_01.tar.gz",  # I explain this later on TODO!!!
    keywords=[
        "COBOL",
        "EBCDIC",
        "CSV",
    ],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        "ebcdic",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
