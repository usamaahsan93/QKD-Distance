#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:19:46 2020

@author: usama
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.close('all')

dispersionCoeff=18
L=np.arange(10,410,10)
spectralWidth=0.6
alpha=0.17

prof=alpha*L

deltaT_chrom=dispersionCoeff*L*spectralWidth/1000

######### PLOTTING #######################
plt.plot(L,deltaT_chrom,'-o',label='Dispersion (ps)')
plt.yscale('log')
plt.plot(L,prof,'k--x',label='Attenuation (dB)')
plt.xlabel('Length of optic fiber (km)',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True,which='both')
plt.legend(fontsize='xx-large')
plt.yticks([0.1,1,10,100],[0.1,1,10,100])

laserPout=-35
laserOPinmW=0.00031622776601683794

loss= 10**(prof/10)
pOut=laserOPinmW/loss

relativeLoss=((laserOPinmW - pOut) / laserOPinmW) *100

pulseWidth=0.3
pulseDisperse=pulseWidth + deltaT_chrom/1000
relativeDisperse = ((pulseDisperse - pulseWidth) / pulseDisperse) * 100

name=['Distance',
      'Attenuation (dB)',
      'Dispersion (ps)',
      'Output Power (mW)',
      'Relative Loss (%)',
      'Pulse Dispersion (ns)',
      'Relative Pulse Dispersion (%)'
      ]
val=[L,
     prof,
     deltaT_chrom,
     pOut,
     relativeLoss,
    
     pulseDisperse,
     relativeDisperse
     ]

df=pd.DataFrame(dict(zip(name,val)))
