#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:40:01 2020

@author: usama
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

plt.close('all')

#Creating array for Poisson curve x axis
n = np.arange(0, 5, 0.1)

#Creating array for different Poisson curves
Mu=np.arange(0.1, 1, 0.1)

lstyle=['-','--','-.',':']

#Evaluating for each mu value
count=0
for mu in Mu:
    idx=count%len(lstyle)
    count=count+1
    #Solving Poisson Curve
    d = np.power(mu, n)*np.exp(-mu)/factorial(n) * 100
    plt.plot(n, d,label='$\mu={0:.2f}$'.format(mu),linestyle=lstyle[idx],linewidth=2.5)#=mrkr[idxMarker],c=clr[idxColor])

#Setting the plotted graph parameters
plt.grid(which='both')
plt.ylim(top=103)
plt.legend(fontsize='x-large')
plt.xlabel('Number of Photons',fontsize=16)
plt.ylabel('Probability (%)',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
