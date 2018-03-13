#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:04:54 2018

@author: armitage
"""

import numpy as np

def dem_difference(dem1,dem2):
    #flatten dem
    flat1 = dem1.flatten()
    flat2 = dem2.flatten()
    
    # difference
    diff = flat2-flat1
    return diff

