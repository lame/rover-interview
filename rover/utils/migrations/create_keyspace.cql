//This should be changed from SimpleStrategy for production clusters
//CQLEngine will not allow tuning of replication class and replication factor

CREATE KEYSPACE rover WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
