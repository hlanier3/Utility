# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:20:30 2020

@author: lanie
"""

import math
import random
import numpy

def dh(n):
    m = random.randint(0,n)
    p = random.randint(0,m)
    print(p, m)
    alice = random.randint(0, p)
    bob = random.randint(0, p)
    print(alice, bob)
    aliceP = ((p % m) ** alice) % m
    bobP = ((p % m) ** bob) % m
    print(aliceP, bobP)
    key = (aliceP ** bobP) % m
    
    return key

def stepOne(n):
    m = random.randint(0,n)
    p = random.randint(0,m)
    return m, p

def stepTwo(m, p):
    x = random.randint(0,p)
    print("Don't share me: " + str(x))
    share = pow(p,x,m)
    print("Share me: " + str(share))
    return x, share

def stepThree(x, y, m):
    print("Your key is: " + str(pow(y,x,m)))
    return "Done"
