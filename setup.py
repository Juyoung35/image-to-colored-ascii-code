from setuptools import setup, find_packages

install_requires = [
    "Pillow==0.9.1",
    "python-docx==0.8.11"
]

setup(
    name="image=-to-colored-ascii-code",
    version="0.1",
    description="This program converts image file to ascii code texts such as .txt, .rtf, .docs, .html",
    author="Juyoung35",
    author_email="justin350518@gmail.com",
    packages=find_packages(),
    install_requires=install_requires
)