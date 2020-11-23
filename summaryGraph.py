#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:19:19 2020

@author: usama
"""

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

Rraw=q * eff * mu * Frep * tlink 


RsiftBB84 = 0.5 * Rraw

effBB84= 0.5 # Eqn 4.7
Rdark=0.01
QBERdark=Rdark/(effBB84 * q * Frep * tlink * eff * mu) *1000


plt.figure();

plt.plot(L,RsiftBB84,'-o',label='$R_{sift}$ of BB84 and KMB09') ;
plt.plot(L,QBERdark,'--*',label='QBER of BB84 and KMB09');

plt.hlines(25,0,L[-1],linestyles='dashed',label='Theoretical $QBER_{eve}$ limit (25%)')
plt.vlines(250,0,max(QBERdark),colors='r',linestyles='dashdot',label='Maximum bearable optic fiber attenuation (250 km)')

plt.vlines(270,0,max(QBERdark),colors='g',label='Threshold based on QBER profile')

plt.yscale('log');
plt.xscale('log');
plt.grid(which='major')

l_km=250
y=np.where(L==l_km)[0][0]

plt.annotate('Optimal Point\n (250,{:.3f})'.format(RsiftBB84[y]),
ha = 'center', va = 'bottom', fontsize=14,
xytext = (120,0.0005),xy = (250, 1.167),arrowprops = {'facecolor' : 'black', 'width':1.5,'headwidth':8})
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Length of optic fiber (km)',fontsize=14)
plt.legend(fontsize='large',loc='upper left',bbox_to_anchor=(0.0, 0.5))#,loc='best',bbox_to_anchor=(0,1,50,50))
plt.yticks([0.0001,0.001,0.01,0.1,1,10,100,1000,10000],[0.0001,0.001,0.01,0.1,1,10,100,1000,10000])

plt.xticks([1,10,100,1000],[1,10,100,1000])


