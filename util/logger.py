import logging


class Logger:
    def __init__(self, logger_name):
        self.logger_name = logger_name
        self.logger = self._configure_logging()

    def _configure_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        logger = logging.getLogger(self.logger_name)
        return logger

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
