#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:28:21 2020

@author: usama
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

alpha=0.17
L=np.arange(0,450,10)
q= 0.5
eff=0.056
mu= 0.1
Frep=15*1e6
tlink= 10**(-alpha*L/10)

#Evaluating Rraw (Ref. corresponding paper)
Rraw=q * eff * mu * Frep * tlink 

RsiftBB84 = 0.5 * Rraw

effBB84= 0.5 # Eqn 4.7
Rdark=0.01

QBERdark=Rdark/(effBB84 * q * Frep * tlink * eff * mu) *1000

plt.figure(); plt.plot(L,RsiftBB84,'-o') ;
plt.yscale('log'); plt.xscale('log');plt.grid(True,which='both')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Length of optic fiber (km)',fontsize=14)
plt.ylabel('$R_{sift}$',fontsize=14)

plt.figure(); plt.plot(L,QBERdark,'-o');
plt.yscale('log'); plt.xscale('log');plt.grid(True,which='both')
plt.xlim(right=500)
plt.xlabel('Length of optic fiber (km)',fontsize=14)
plt.ylabel('QBER (%)',fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.figure(); plt.plot(L,QBERdark,'-.x',label=r'$QBER_{dark} (\%)$');
plt.plot(L,RsiftBB84,'-o',label=r'$R_{sift_{KMB09}} (bps)$');
plt.yscale('log'); 
plt.xscale('log')
plt.grid(True,which='both')
plt.xlim(right=500)
plt.xlabel('Length of optic fiber (km)',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize='x-large')
plt.yticks([0.0001,0.001,0.01,0.1,1,10,100,1000,10000,100000],[0.0001,0.001,0.01,0.1,1,10,100,1000,10000,10000])
plt.xticks([1,10,100,1000],[1,10,100,1000])
