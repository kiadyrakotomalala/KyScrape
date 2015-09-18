'''
Created on 5 sept. 2015
@author: RAVAHATRA Kiady
'''
from selenium import webdriver
import threading
import Queue
from bs4 import BeautifulSoup
import requests
from Configuration import Configuration

def getPage(url):
    return BeautifulSoup(requests.get(url).text)


class DownloaderWorker (threading.Thread):
    def __init__(self, threadID, name, q, multiThreadMotor):        
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        self.multiThreadMotor = multiThreadMotor
        
    def run(self):
        if Configuration().selenium: 
            self.launchBrowser()
        self.process_data(self.name, self.q)
    
    def launchBrowser(self):
        self.browser = webdriver.PhantomJS()

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
        print 'Downloading {0}'.format(self.element.url)
        try:
            if Configuration().selenium:
                self.browser.get(self.element.url)
                self.element.setSoup(BeautifulSoup(self.browser.page_source))
            else:
                self.element.setSoup(getPage(self.element.url))
            self.multiThreadMotor.main.actioner.addElement(self.element)
        except:
            print 'error'
            self.element.error = True

class DownloaderMotor(threading.Thread):
    def __init__(self, main):
        threading.Thread.__init__(self)
        self.main = main
        self.threadList = range(0,Configuration().numberDownloader)
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
        #print 'New element to download'
        self.queueLock.acquire()
        self.workQueue.put(element)
        self.queueLock.release()
    
        
    def run(self):
        for tName in self.threadList:
            thread = DownloaderWorker(self.threadID, tName, self.workQueue, self)
            thread.start()
            self.threads.append(thread)
            self.threadID += 1
                
        while not self.workQueue.empty():
            pass
               
        self.exitFlag = 1
        
        for t in self.threads:
            t.join()
        
        print 'on downloader'