import pickle
from Configuration import Configuration
import os

#Element class: definition of all objects to be passed to all workers
class Element():
    def __init__(self, parent, deep, url):
        self.parent = parent
        self.deep = deep
        self.url = url
        self.finished = False
        self.data = {}

    def setFinished(self):
        self.finished = True
    
    def setSoup(self, soup):
        self.soup = soup
    
    def setData(self, data):
        self.data = data
        
    def store(self):
        print "writing {0}".format(self.data['name'].replace('/',''))
        i = 1
        if not os.path.isfile('{0}/{1}'.format(Configuration().outputDirectory,self.data['name'].replace('/',''))):
            pickle.dump(self.data, file('{0}/{1}'.format(Configuration().outputDirectory,self.data['name'].replace('/','')),'w'))
        else:
            while True:
                if not os.path.isfile('{0}/{1}_{2}'.format(Configuration().outputDirectory,self.data['name'].replace('/',''),i)):
                    pickle.dump(self.data, file('{0}/{1}_{2}'.format(Configuration().outputDirectory,self.data['name'].replace('/',''),i),'w'))
                    break
                else:
                    i = i+1