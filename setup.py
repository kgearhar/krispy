import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="krispy", # Replace with your own username
    version="1.0.4",
    author="Kristen Gearhart",
    author_email="kgears502@gmail.com",
    description="ahp trade study tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kgearhar/krispy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'numpy>=1.19.0',
        'matplotlib>=3.2.2',
    ]
)