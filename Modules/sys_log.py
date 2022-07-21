import logging as logg
import os

_FILE = os.path.abspath("System_log/")

logg.basicConfig(
    level= logg.WARNING,
    format= "%(asctime)s %(levelname)s ::%(filename)s:: [%(funcName)s] Line: %(lineno)d ==> %(message)s",
    datefmt= "%I:%M:%S",
    handlers= [
        logg.FileHandler(f"{_FILE}\data.log"),
        logg.StreamHandler()
    ]
)

if __name__ == "__main__":
    logg.info("test")
    logg.warning("test")
    logg.error("test")
    logg.critical("test")