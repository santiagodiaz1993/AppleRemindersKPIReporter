from setuptools import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-sdiaz19",
    license="MIT",
    version="0.0.1",
    author="Santiago-Diaz",
    keyword="reporter",
    author_email="sdiaz19@binghamton.edu",
    description="Create reports for the Apple Reminders app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/santiagodiaz1993/AppleRemindersKPIReporter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
