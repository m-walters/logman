import logging

class logman:
    def __init__(self, name, level, logfile, sformat):
        level = level.upper() 
        self.name = name 
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handle = logging.FileHandler(logfile)
        handle.setLevel(getattr(logging, level))
        handle.setFormatter(logging.Formatter(sformat))
        self.logger.addHandler(handle)


    def add_handler(self, level, sformat, fname=None):
        level = level.upper() 
        logging.getLogger(self.name) 
        if not fname:
            ch = logging.StreamHandler()
            ch.setLevel(getattr(logging, level))
            ch.setFormatter(logging.Formatter(sformat))
            self.logger.addHandler(ch)
        else:
            fh = logging.FileHandler(fname)
            fh.setLevel(getattr(logging, level))
            fh.setFormatter(logging.Formatter(sformat))
            self.logger.addHandler(fh) 


    def printl(self, level, msg):
        level = level.lower() 
        getattr(self.logger, level)(msg)

