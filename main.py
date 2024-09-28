from loguru import logger

from src.utils import load_yaml, check_dir, read_version
from src.backup_timer import BackupTimer

if __name__ == '__main__':
    # Version info
    version = read_version('./VERSION')
    logger.info(f'Version: {version}')

    # Config info
    config = load_yaml('./config.yml')
    logger.info(f'Time interval: {config["interval"]} minutes')
    logger.info(f'Backup Dir: {config["input"]}')
    logger.info(f'Save to: {config["output"]}')
    logger.info(f'Is zip: {config["is_zip"]}')
    check_dir(config['output'])

    # Init loguru
    logger.add(
        "./logs/{time}.log",
        rotation=config['loguru']['rotation'],
        retention=config['loguru']['retention'],
        compression=config['loguru']['compression']
    )
    logger.info("BackupTimer initialized")

    # Begin BackupTimer
    bt = BackupTimer(
        config['interval'],
        config['input'],
        config['output'],
        config['is_zip']
    )

    try:
        bt.run()
        bt.stop_event.wait()
    except KeyboardInterrupt:
        bt.stop()
        logger.info("Backup process interrupted and stopped.")
