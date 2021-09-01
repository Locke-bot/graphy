# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 06:24:10 2021

@author: Zen
"""

import pytesseract

print(pytesseract.image_to_string("x_scale.png").strip())