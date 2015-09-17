'''
Created on 9 sept. 2015

@author: RAVAHATRA Kiady
'''

import petl as etl
import os
import pickle

def loadData(path):
    liste = []    
    for (dirpath, dirnames, fnames,) in os.walk(path):
        liste.extend([ os.path.join(path, fname) for fname in fnames ])
        break    
    allData = []
    for l in liste:
        try:
            allData.append(pickle.load(file(l)))
        except:
            pass
    return allData

def writeData():
    etl.tocsv([x.values() for x in loadData('result')], 'example.csv')

writeData()