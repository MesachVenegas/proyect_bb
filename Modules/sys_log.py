import logging as logger
import os

_FILE = os.path.abspath("System_log/")

logger.basicConfig(
    level= logger.INFO,
    format= "%(asctime)s %(levelname)s ::%(filename)s:: [%(funcName)s] Line: %(lineno)d ==> %(message)s",
    datefmt= "%I:%M:%S",
    handlers= [
        logger.FileHandler(f"{_FILE}\data.log"),
        logger.StreamHandler()
    ]
)

if __name__ == "__main__":
    logger.info("test")
    logger.warning("test")
    logger.error("test")
    logger.critical("test")