#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:11:54 2020

@author: usama
"""
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

# Making an array from 0 to 2pi 
theta=np.arange(0,2*np.pi,0.001)

#Calculating the efficiency considering the following formula from KXB10 paper (https://arxiv.org/pdf/1112.1110.pdf)
a=((np.sin(theta/2))**2)/2 

#Finding maximum value of efficiency
x=np.where(a==max(a))[0][0]

#Plotting the values and optimal point
plt.plot(theta,a,'-')

plt.grid()
plt.xlabel('$\\theta_{KMB09}$',fontsize=14)
plt.ylabel('$\eta_{KMB09}$',fontsize=14)

plt.scatter(theta[x],max(a),c='r',label='Max point ({0:.3f},{1:.3f})'.format(theta[x],max(a)))
plt.legend(fontsize='xx-large')
locs, labels=plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi $'])
