from logger import logger
class file_logger(logger):

    file_name = "file_log.txt"

    def __init__(self, log_level):
        logger.__init__(self, log_level)

    def log(self, log_level, message):
        f = open(self.file_name, "w+")        
        f.write(str(log_level) + ": " + message)
        f.close()

    def set_file_name(self, file_name):
        self.file_name = file_name