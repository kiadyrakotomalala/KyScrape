'''
Created on 5 sept. 2015
@author: RAVAHATRA Kiady
'''

from Downloader import DownloaderMotor
import Actioner 
import Writer
import os
from Element import Element
from Configuration import Configuration

class Main():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Main, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.downloader = DownloaderMotor(self)
        self.downloader.start()
        self.actioner = Actioner.ActionerMotor(self)
        self.actioner.start()
        self.writer = Writer.WriterMotor()
        self.writer.start()

main = Main()
main.downloader.addElement(Element(None,0,Configuration().mainUrl))

try:
    os.makedirs(Configuration().outputDirectory)
except:
    pass