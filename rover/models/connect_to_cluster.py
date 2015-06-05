from cqlengine import connection
from config import cassandra_cluster_ip, cassandra_default_keyspace


class Conn:
    def __init__(self):
        """
        This class will create a connection with CQLEngine to
        the cassandra db provided in the config file. Will not
        reactivate a session if one is active already
        """
        if connection.get_session() is None:
            connection.setup([cassandra_cluster_ip], cassandra_default_keyspace)
