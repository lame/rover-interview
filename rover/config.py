import os

basedir = os.path.abspath(os.path.dirname(__file__))
script_dir = os.path.dirname(__file__)

CSRF_ENABLED = True
SECRET_KEY = 'Replace_With_SecretKey'
# TODO<Ryan>: Change this to a command line argument
cassandra_cluster_ip = '127.0.0.1'
cassandra_default_keyspace = 'rover'
