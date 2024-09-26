import os
import time
import shutil
import threading

from loguru import logger


class BackupTimer:
    def __init__(self, interval: int, input_dir: str, output_dir: dir):
        if not os.path.exists(input_dir):
            logger.error(f'Input dir is not found.')
            exit(1)
        if interval < 0:
            logger.error(f'Timer interval must be > 0.')

        self.interval = interval
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.format = "%Y%m%d_%H%M%S"

        self.timer = None
        self.stop_event = threading.Event()

    def run(self) -> None:
        self.timer = threading.Timer(self.interval * 60, self.backup)
        self.timer.start()

    def backup(self) -> None:
        curr_time = time.strftime(self.format, time.localtime())
        logger.info(f"\nBackup time: {curr_time}")

        zip_file_name = os.path.join(self.output_dir, f"backup_{curr_time}.zip")
        try:
            shutil.make_archive(zip_file_name.replace('.zip', ''), 'zip', self.input_dir)
            logger.info(f"Folder '{self.input_dir}' has been compressed to '{zip_file_name}'")
        except Exception as e:
            logger.error(f"Error while compressing folder: {e}")

        self.run()

    def stop(self) -> None:
        if self.timer is not None:
            self.timer.cancel()
        self.stop_event.set()
        logger.info("BackupTimer stopped")
