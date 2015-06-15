import os
import unittest
from unittest import TestCase

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from app import app
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from config import cassandra_cluster_ip, cassandra_default_keyspace
from models.connect_to_cluster import Conn
from utils.data.scheduled_processes import CalculateSitterRating
from uuid import UUID


class ScoringTest(TestCase):

    def create_app(self):
        self.app = app.test_client()
        return app

    def setUp(self):
        Conn()
        """
        Setup the cassandra connection and Batch
        """
        cluster = Cluster([cassandra_cluster_ip])
        self.session = cluster.connect(cassandra_default_keyspace)

        self.insert_rating_by_sitter = self.session.prepare('INSERT INTO rating_by_sitter\
                                                            (sitter_id, rating, id)\
                                                            VALUES (?, ?, ?)')
        self.batch = BatchStatement()
        """
        Create reviews
        """
        # test 1 review
        self.batch.add(self.insert_rating_by_sitter, (1, 5, UUID('{60045a7a-168d-47e0-8780-4511f6b2dbf1}')))
        # test 9 reviews
        for x in range(9):
            id = ('{{60045a7a-168d-47e0-8780-4511f6b2dcf{0}}}'.format(x))
            self.batch.add(self.insert_rating_by_sitter, (2, 5, UUID(id)))
        # test 10 reviews
        for x in range(10):
            id = ('{{60045a7a-168d-47e0-8780-4511f6b2ddf{0}}}'.format(x))
            self.batch.add(self.insert_rating_by_sitter, (3, 5, UUID(id)))
        self.session.execute(self.batch)

    def tearDown(self):
        for x in range(3):
            self.session.execute('DELETE FROM rating_by_sitter WHERE sitter_id = {0}'.format(x+1))

    def test_no_reviews(self):
        self.assertEqual(CalculateSitterRating.get_sitter_rating_by_id(self, 0, 2.5,
                                                                       self.session.execute('SELECT rating\
                                                                                            FROM rating_by_sitter\
                                                                                            WHERE sitter_id = 0')), 2.5)

    def test_one_review(self):
        self.assertEqual(CalculateSitterRating.get_sitter_rating_by_id(self, 1, 2.5,
                                                                       self.session.execute('SELECT rating\
                                                                                            FROM rating_by_sitter\
                                                                                            WHERE sitter_id = 1')), 2.75)

    def test_nine_reviews(self):
        self.assertEqual(CalculateSitterRating.get_sitter_rating_by_id(self, 2, 2.5,
                                                                       self.session.execute('SELECT rating\
                                                                                            FROM rating_by_sitter\
                                                                                            WHERE sitter_id = 2')), 4.75)

    def test_ten_reviews(self):
        self.assertEqual(CalculateSitterRating.get_sitter_rating_by_id(self, 3, 2.5,
                                                                       self.session.execute('SELECT rating\
                                                                                            FROM rating_by_sitter\
                                                                                            WHERE sitter_id = 3')), 5)


if __name__ == '__main__':
    unittest.main()
