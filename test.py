import argparse
import PIL
import numpy
import scipy
import docx

for package in [argparse, PIL, numpy, scipy, docx]:
    print(f"package {package} version is {package.__version__}")