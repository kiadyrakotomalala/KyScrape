import Action

class Configuration():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Configuration, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.numberDownloader = 20
        self.numberActioner = 10
        self.numberWriter = 20
        
        self.mainUrl = "http://www.annumada.com/index.php?option=com_annupagesjaunes&list=theme&lang=fr"
#        self.mainUrl = "http://www.annumada.com/index.php?option=com_annupagesjaunes&list=societe&theme=7&rubrique=366&ville=44&lang=fr"
        self.actionList = [Action.Action1, Action.Action2,Action.Action3,Action.Action4]
        self.outputDirectory = 'result'
