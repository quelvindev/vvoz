import logging
from pathlib import Path



class LogConfig:
    def __init__(self, filename='vvoz.log', filemode='a', level=logging.DEBUG,dir_log = None):
        self.home = Path.home()
        self.source = Path(self.home.anchor)
        self.my_folder_log = 'vvideo_log'
        default_log_dir =  Path(Path.home().anchor)/'vvoz_log' if dir_log is None else Path(dir_log)
        default_log_dir.mkdir(parents=True,exist_ok=True)
        folder = default_log_dir/filename

        self.logger = logging.getLogger(str(folder))
        self.logger.setLevel(level)

        if not self.logger.handlers:
            handler = logging.FileHandler(folder, mode=filemode)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.create_folder_log()

    def create_folder_log(self):

        folder = self.source /self.my_folder_log
        folder.mkdir(exist_ok=True)
        self.dir_log = folder
        return self.dir_log


    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
