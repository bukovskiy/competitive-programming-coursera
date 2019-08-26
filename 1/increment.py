#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 01:13:43 2019

@author: vladimiruspenskiy
"""

import sys
import math

def main():
    x = input()
    result = len(x)
#    print(len(str(x)))
#    print(math.log10(x+1))
#    print(math.floor(math.log10(x+1))+1)
    for c in x:
        if c=="9":
            continue
        else:
            return print(result)
    print(result+1)
if __name__ == '__main__':
    main()
