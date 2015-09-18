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

def getTable(path):
    return etl.fromdicts(loadData(path))

def writeDataToCsv(path, output):
    etl.tocsv(getTable(path), output)

def writeDataToJson(path, output):
    etl.tojson(getTable(path), output)

def writeDataToXls(path, output):
    etl.toxls(getTable(path), output, 'sheet1', 'utf-8')

writeDataToXls('result', 'result.xls')