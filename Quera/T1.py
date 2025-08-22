# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 16:10:26 2023

@author: ALI
"""

a = int(input())
b = list()
for i in range(a):
    b.append(input())

for j in b:
    c = j.split()
    d = set(c[0] + c[1])
    
    if (set(c[2]).issubset(d)) or (set(c[2]).issubset(set("O-"))) or \
        (set(c[2]).issubset(set("O+"))) or ((set(c[2][:-1]).issubset(d)) and set("-").issubset(set(c[2]))):
        print("valid")
    else:
        print("invalid")
        