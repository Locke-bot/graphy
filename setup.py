# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 08:24:31 2021

@author: Unrated
"""

from distutils.core import setup
from Cython.Build import cythonize

# setup(ext_modules=cythonize('cyscaler.pyx', language_level='3', annotate=True))
setup(ext_modules=cythonize('cygaussian.pyx', language_level='3', annotate=True))
# setup(ext_modules=cythonize('cygaussianpro.pyx', language_level='3', annotate=True))