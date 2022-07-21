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

    # Crea y regesa un objeto de conexion.
    @classmethod
    def pool_connexion(cls):
        connection = Connection.make_pool().getconn()
        return connection

    # Libera la conexion para devolverla al pool de conexiones.
    @classmethod
    def free_pool(cls, conexion):
        free : Connection.make_pool().putconn(conexion)
        logger.info(f"{cls._pool} Liberado")
        return free

    # Cierra el pool de conexiones.
    @classmethod
    def finish_pool(cls):
        Connection.make_pool().closeall()
        logger.info(f"{cls._pool} Cerrado")