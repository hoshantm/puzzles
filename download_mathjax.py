#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:29:12 2024

@author: tarik
"""

import requests
import os

baseUrl="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/" #Base URL for the main directory
#List containing relative paths of all required files
relativePaths=['config/Safe.js?V=2.7.5',
       'config/TeX-AMS-MML_HTMLorMML.js?V=2.7.5',
       'extensions/Safe.js?V=2.7.5',
       'jax/output/SVG/fonts/TeX/fontdata.js?V=2.7.5',
       'jax/output/SVG/jax.js?V=2.7.5',
       'MathJax.js?config=TeX-AMS-MML_HTMLorMML%2CSafe.js&#038;ver=4.1']

parentDir='\\'.join(baseUrl.split('/')[-3:]) #Parent directory from URL
for path in relativePaths: #For all files
    req=requests.get(baseUrl+path) #forming url

    filename=path.split("/")[-1].split("?")[0] #extracting filename out of url
    directory=os.path.join(parentDir,"\\".join(path.split('/')[:-1])) #Extracting directories path for local path formation
    if not os.path.exists(directory): #Creating local direcories if they do not exist
        os.makedirs(directory)

    with open(os.path.join(directory,filename),"wb+") as file: #Storing results into files
        file.write(req.content)