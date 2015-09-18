'''
Created on 5 sept. 2015
@author: RAVAHATRA Kiady
'''

import threading
import Queue
from Configuration import Configuration

class WriterWorker (threading.Thread):
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
            try:
                self.multiThreadMotor.queueLock.acquire()
        
                if not self.multiThreadMotor.workQueue.empty():
                    self.element = self.q.get()
                    self.multiThreadMotor.queueLock.release()
                    self.treat()
    
                else:
                    self.multiThreadMotor.queueLock.release()
            except:
                pass
    
    def treat(self):
        print 'Writing {0}'.format(self.element.url)
        self.element.store()
        self.element.setFinished()


class WriterMotor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.threadList = range(0, Configuration().numberActioner)
        self.queueLock = threading.Lock()
        self.workQueue = Queue.Queue()
        self.threads = []
        self.threadID = 1
        self.exitFlag = 0


    def addElement(self, element):
        print 'New element to write'
        self.queueLock.acquire()
        self.workQueue.put(element)
        self.queueLock.release()


    def run(self):
        for tName in self.threadList:
            thread = WriterWorker(self.threadID, tName, self.workQueue, self)
            thread.start()
            self.threads.append(thread)
            self.threadID += 1
                
        while not self.workQueue.empty():
            pass
               
        # Notify threads it's time to exit
        self.exitFlag = 1
        
        for t in self.threads:
            t.join()
        
        print 'end writer'