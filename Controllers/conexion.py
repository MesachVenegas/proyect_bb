from psycopg2 import pool
from Modules.sys_log import logger
import sys

class Connection:

    _DBNAME = "project_bb"
    _HOST = "localhost"
    _DBPORT = "5432"
    _USER = "postgres"
    _PASSWORD = "admin"
    _MIN = 1
    _MAX = 5
    _pool = None

    #  Crea un pool de conexiones a la base de datos.
    @classmethod
    def make_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN,
                    cls._MAX,
                    user = cls._USER, password = cls._PASSWORD, host = cls._HOST, port = cls._DBPORT, dbname = cls._DBNAME
                    )
                logger.info(f"Conexion Establecida: {cls._pool}")
                return cls._pool
            except Exception as fail:
                logger.error(f"{fail}")
                sys.exit()
        else:
            return cls._pool