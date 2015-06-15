# Bisect should be used in refactoring for increased performance
# import bisect
import os
import sched
import time

parentdir = os.path.abspath(os.curdir)
os.sys.path.insert(0, parentdir)

from app import app
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from config import cassandra_cluster_ip, cassandra_default_keyspace

"""
This file needs to be runs as a separate process,
in production this should be added in as a hook
"""


class Scheduler:
    """
    With cassandra, it is inefficient to create
    a 'count' or average that requires a read-write.
    Because it is not program essential to have this
    be an exact number all the time, it is a perfect
    candidate for a batch update. This can be tuned to
    update as frequently as desired.
    """
    # FIXME: Needs to be threaded
    def __init__(self):
        s = sched.scheduler(time.time, time.sleep)
        s.enter(9, 1, self.run_scheduled_processes, (s,))
        s.run()

    def run_scheduled_processes(self, sc):
        sc.enter(9, 1, self.run_calculate_sitter_rating, (sc,))
        sc.enter(9, 2, self.run_sorted_sitter_by_rating, (sc,))
        sc.enter(9, 3, self.run_scheduled_processes, (sc,))
        sc.run()

    def run_calculate_sitter_rating(*args, **kwargs):
        print('running calc sitter rating')
        CalculateSitterRating()

    def run_sorted_sitter_by_rating(*args, **kwargs):
        print('running sorted sitter by rating')
        SortedSitterByRating()


class CalculateSitterRating:
    """
    This class will pull all unique sitter_id's from
    the sitter_profile col_fam, pull all review integers
    of that sitter from rating_by_sitter col_fam and
    and calculate the appropriate sitter rating. This has
    to be done through the python-driver instead of
    CQLEngine due to restrictions on ModelQuerySet
    """
    def __init__(self):
        #  Connect to cassandra cluster and keyspace
        cluster = Cluster([cassandra_cluster_ip])
        self.session = cluster.connect(cassandra_default_keyspace)
        self.insert_sitter_profile = self.session.prepare('INSERT INTO sitter_profile\
                                                          (id, rating)\
                                                          VALUES (?, ?)')
        self.batch = BatchStatement()
        self.update_rating()

    def update_rating(self):
        rows = self.session.execute('SELECT id, score FROM sitter_profile')
        for row in rows:
            reviews = self.session.execute('SELECT rating FROM rating_by_sitter\
                                           WHERE sitter_id = {0}'.format(row.id))
            weighted_rating = self.get_sitter_rating_by_id(row.id, row.score, reviews)
            self.batch.add(self.insert_sitter_profile, (row.id, weighted_rating))
        self.session.execute(self.batch)

    def get_sitter_rating_by_id(self, id, score, reviews):
        calc_rating = 0.0
        total_reviews = 0

        for review in reviews:
            total_reviews += review.rating

        if len(reviews) == 0:
            calc_rating = score
        elif len(reviews) > 0 and len(reviews) < 10:
            weight_factor = (((total_reviews / len(reviews)) - score) / 10)
            calc_rating = ((weight_factor * len(reviews)) + score)
        else:
            calc_rating = total_reviews / len(reviews)
        return calc_rating


class SortedSitterByRating:
    """
    Creating a batch statement for inserting multiple
    rows into the table at once, provides substantial
    performance enhancements.
    """

    def __init__(self):
        self.sorted_list = []
        cluster = Cluster([cassandra_cluster_ip])
        self.session = cluster.connect(cassandra_default_keyspace)

        self.insert_sitter_sorted = self.session.prepare('INSERT INTO sitters_by_rating\
                                                         (overall_rank, rating, sitter_id)\
                                                         VALUES (?, ?, ?)')
        self.batch = BatchStatement()
        self.set_sitters_by_rating_table()
        self.session.execute(self.batch)

    def getKey(self, item):
        return item[0]

    def set_sitters_by_rating_table(self):
        for counter, sitter in enumerate(self.get_all_sitters()):
            self.batch.add(self.insert_sitter_sorted, ((counter+1), sitter[0], sitter[1]))

    def get_all_sitters(self):
        rows = self.session.execute('SELECT rating, id FROM sitter_profile')
        for row in rows:
            self.sorted_list.append((row.rating, row.id))
        return sorted(self.sorted_list, key=self.getKey, reverse=True)


if __name__ == "__main__":
    Scheduler()
