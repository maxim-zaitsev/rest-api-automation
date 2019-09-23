import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def log(self, value):
        self.logger.info(value)
