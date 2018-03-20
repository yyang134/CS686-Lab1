from logger import logger
class stdout_logger(logger):

    def __init__(self, log_level):
        logger.__init__(self, log_level)

    def log(self, log_level, message):
        print(str(log_level) + ": " + message)