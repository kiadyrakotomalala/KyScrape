import Action

class Configuration():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Configuration, cls).__new__(cls)
        return cls.instance

    def __init__(self):
#Number of Thread Downloader
        self.numberDownloader = 5
#Number of Thread Actioner
        self.numberActioner = 10
#Number of Thread Writer
        self.numberWriter = 20

#Main Url: For action1
        self.mainUrl = "http://www.annumada.com/index.php?option=com_annupagesjaunes&list=theme&lang=fr"

#All Actions ---> need to be ordered
        self.actionList = [Action.Action1, Action.Action2,Action.Action3,Action.Action4]

#Output directory
        self.outputDirectory = 'result'

#Use selenium or not (selenium needed for js rendered page)
        self.selenium = False