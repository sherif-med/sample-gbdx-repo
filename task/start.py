#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:02:30 2019

@author: admin2
"""

from gbdxtools import CatalogImage, WV03_VNIR

if __name__ == "__main__":    
    img = CatalogImage('104001001BA7C400')
    print(img.shape, img.bounds)
    print(isinstance(img, WV03_VNIR))