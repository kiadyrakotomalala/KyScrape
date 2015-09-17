'''
Created on 5 sept. 2015
@author: RAVAHATRA Kiady
'''

import threading
import Queue
from Configuration import Configuration
from Element import Element

class ActionerWorker (threading.Thread):
    def __init__(self, threadID, name, q, multiThreadMotor):
        self.configuration = Configuration()
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        self.multiThreadMotor = multiThreadMotor

    def run(self):
        self.process_data(self.name, self.q)

    def process_data(self,threadName, q):
        while True:
            self.multiThreadMotor.queueLock.acquire()
    
            if not self.multiThreadMotor.workQueue.empty():
                self.element = self.q.get()
                self.multiThreadMotor.queueLock.release()
                self.treat()

            else:
                self.multiThreadMotor.queueLock.release()
    
    def treat(self):
        print 'Actioning {0}'.format(self.element.url)
        temp = self.configuration.actionList[self.element.deep](self.element.soup)
        if isinstance(temp, list):
            for url in temp:
                newElem = Element(self.element,self.element.deep+1,url)
                self.multiThreadMotor.main.downloader.addElement(newElem)
        else:
            self.element.setData(temp)
            self.multiThreadMotor.main.writer.addElement(self.element)
            
        self.element.setFinished()



class ActionerMotor(threading.Thread):
    def __init__(self, main):     
        threading.Thread.__init__(self)
        
        self.main = main
        self.threadList = range(0, Configuration().numberActioner)
        self.queueLock = threading.Lock()
        self.workQueue = Queue.Queue()
        self.threads = []
        self.threadID = 1
        self.exitFlag = 0
        #Add element into Queue Object
#         self.queueLock.acquire()
#         for element in listTask:
#             self.workQueue.put(element)
#         self.queueLock.release()
    
    
    def addElement(self, element):
        print 'New element to action , deep = {0}'.format(element.deep)
        self.queueLock.acquire()
        self.workQueue.put(element)
        self.queueLock.release()
    
        
    def run(self):
        for tName in self.threadList:
            thread = ActionerWorker(self.threadID, tName, self.workQueue, self)
            thread.start()
            self.threads.append(thread)
            self.threadID += 1
                
        while not self.workQueue.empty():
            pass
               
        # Notify threads it's time to exit
        self.exitFlag = 1
        
        for t in self.threads:
            t.join()
        
        print 'end actioner'