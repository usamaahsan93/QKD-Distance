#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:30:33 2020

@author: usama
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial


def poissonDistribution():
    st.header('Photon Source')
    st.markdown('---')
    st.write('Photon source follows poisson distribution.')
    st.sidebar.header('Photon Source')
    
    mu = st.sidebar.slider("Expected Value of Photon", 0.0, 2.0, 0.1, step=0.1)
                         
    n = np.arange(0, 5, 0.1)

    d=np.power(mu, n)*np.exp(-mu)/factorial(n) * 100
    
    plt.plot(n, d,label='$\mu={0:.2f}$'.format(mu))
    plt.grid(which='both')
    plt.ylim([0,100])
    plt.legend(fontsize='x-large')
    plt.xlabel('Number of Photons',fontsize=16)
    plt.ylabel('Probability (%)',fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    st.pyplot()
    return mu

def ofcProperties():
    st.header('Optical Fiber Communication')
    st.markdown('---')
    st.write('Inherent attenuation and dispersion in optical fiber.')
    st.sidebar.header('Optical Fiber Properties')
        
    alpha=st.sidebar.slider("Attenuation Coefficient Alpha",0.0,1.0,0.17,step=0.01)

    spectralWidth=st.sidebar.slider('Spectral Width',0.0,1.0,0.6,0.1)
    dispersionCoeff=st.sidebar.number_input('Dispersion Coefficient',min_value=0.0,value=18.0,step=0.1)
    
    L=np.arange(10,410,10)
    prof=alpha*L
    
    deltaT_chrom=dispersionCoeff*L*spectralWidth/1000
    
    plt.plot(L,deltaT_chrom,'-*r',label='Dispersion at (Sp. Wd , Dispr.Coeff)=({:0.2f},{:0.2f})'.format(spectralWidth,dispersionCoeff))
     
    plt.plot(L,prof,'-ob',label='Attenuation at alpha='+str(alpha))
    
    
    log=st.sidebar.checkbox('Set y-axis to log scale')
    if log:
        plt.yscale('log')
    plt.xlabel('Length of optic fiber (km)',fontsize=16)
    plt.ylabel('Attenuation Loss  (dB)',fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    # plt.ylim([1,130])
    plt.grid(True,which='both')
    plt.legend()
    st.pyplot()
    return alpha,spectralWidth,dispersionCoeff
    
st.title('Analysis of achievable distances of BB84 and KMB09 QKD protocols')
st.markdown('---')
st.markdown('''
         This is the research conducted at National Center for Cyber Security (NCCS) Internet Security and Quantum Technology (ISQT) Lab and published in
         [International Journal of Quantum Information](https://www.worldscientific.com/worldscinet/ijqi).
         The research paper for this work can be found [here](https://doi.org/10.1142/S0219749920500331).
         The source code for this project can be found at [Github](https://github.com/usamaahsan93/QKD-Distance).
         
         Authors of this paper are:
         
         Muhammad Mubashir Khan
         &nbsp&nbsp
         [![LinkedIn](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/linkedin-16x16.png)](https://www.linkedin.com/in/muhammad-mubashir-khan-251a802b/)
         &nbsp&nbsp
         [![ORCID](https://ndownloader.figshare.com/files/8439032/preview/8439032/preview.jpg)](https://orcid.org/0000-0002-0011-9525)         
         
         Asad Arfeen
         &nbsp&nbsp
         [![ORCID](https://ndownloader.figshare.com/files/8439032/preview/8439032/preview.jpg)](https://orcid.org/0000-0002-2419-6621)
         
         Usama Ahsan
         &nbsp&nbsp
         [![LinkedIn](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/linkedin-16x16.png)](https://www.linkedin.com/in/usamaahsan93/)
         &nbsp&nbsp
         [![ORCID](https://ndownloader.figshare.com/files/8439032/preview/8439032/preview.jpg)](https://orcid.org/0000-0002-4245-9851)
         &nbsp;&nbsp
         [![GitHub](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/github-16x16.png)](https://github.com/usamaahsan93)
         &nbsp;&nbsp
         [![Goodreads](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/goodreads-16x16.png)](https://www.goodreads.com/usamaahsan93)

         
         Saneeha Ahmed
         
         Tahreem Mumtaz

         ''')
         

mu=poissonDistribution()
alpha,spectralWidth,dispersionCoeff=ofcProperties()

st.header(r'QBER and $R_{SIFT}$')
st.markdown('---')
st.write('QBER and Rsift can be evaluated based on laser properties and protocol efficiency.')
st.sidebar.header('Laser Properties')

L=np.arange(0,450,10)
q=st.sidebar.number_input('Encoding Efficiency',0.0,1.0,0.5,step=0.1)
eff=st.sidebar.number_input('Detector Efficiency',0.0,1.0,0.056,step=0.1)

Frep=st.sidebar.number_input('Frequency of Photon Repetition (kHz)',0.0,value=15.0)
Frep=Frep*1e6
pEff=st.sidebar.number_input('Protocol Efficiency',0.0,1.0,0.5,step=0.1)

tlink= 10**(-alpha*L/10)
Rraw=q * eff * mu * Frep * tlink 
Rsift = 0.5 * Rraw

Rdark=st.sidebar.number_input('Detector Dark Count Rate',0.0, value=0.01,step=0.01)

QBERdark=Rdark/(pEff * q * Frep * tlink * eff * mu) *1000

plt.plot(L,QBERdark,'-.x',label=r'$QBER_{dark} (\%)$');
plt.plot(L,Rsift,'-o',label=r'$R_{sift_{KMB09}} (bps)$');
xlog=st.sidebar.checkbox('Set  x-axis to log scale')
if xlog:
    plt.xscale('log'); 

ylog=st.sidebar.checkbox('Set  y-axis to log scale')
if ylog:
    plt.yscale('log')
plt.grid(True,which='both')

plt.xlabel('Length of optic fiber (km)',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize='x-large')
# plt.yticks([0.0001,0.001,0.01,0.1,1,10,100,1000,10000,100000],[0.0001,0.001,0.01,0.1,1,10,100,1000,10000,10000])
# plt.xticks([1,10,100,1000],[1,10,100,1000])
st.pyplot()

st.header('QKD Distance Summary')
st.markdown('---')
###################################################
st.write("Summary of QBER and Rsift under specified protocol efficiency and specified onfigurations")

st.sidebar.header('Summary')
effBB84=st.sidebar.slider("Protocol Efficiency",0.0,1.0,0.5,step=0.01)

QBERdark=Rdark/(effBB84 * q * Frep * tlink * eff * mu) *1000

plt.figure();

plt.plot(L,Rsift,'-o',label='$R_{sift}$ of BB84 and KMB09') ;
plt.plot(L,QBERdark,'--*',label='QBER of BB84 and KMB09');

plt.hlines(25,0,L[-1],linestyles='dashed',label='Theoretical $QBER_{eve}$ limit (25%)')
plt.vlines(250,0,max(QBERdark),colors='r',linestyles='dashdot',label='Maximum bearable optic fiber attenuation (250 km)')

plt.vlines(270,0,max(QBERdark),colors='g',label='Threshold based on QBER profile')

plt.yscale('log');
plt.xscale('log');
plt.grid(which='major')

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Length of optic fiber (km)',fontsize=14)
plt.legend(fontsize=9,loc='upper left',bbox_to_anchor=(0.0, 0.5))#,loc='best',bbox_to_anchor=(0,1,50,50))
plt.yticks([0.0001,0.001,0.01,0.1,1,10,100,1000,10000],[0.0001,0.001,0.01,0.1,1,10,100,1000,10000])

plt.xticks([1,10,100,1000],[1,10,100,1000])
st.pyplot()
