import csv
import os
import unittest
from unittest import TestCase

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentdir)
os.sys.path.insert(0, parentdir)

from app import app
# from models.csv_import import CSVImport
from models.connect_to_cluster import Conn
from models.owner_by_sitter import OwnerBySitter
from models.owner_name_by_id import OwnerNameByID
from models.owner_profile import OwnerProfile
from models.rating_by_sitter import RatingBySitter
from models.sitter_by_owner import SitterByOwner
from models.sitter_name_by_id import SitterNameByID
from models.sitter_profile import SitterProfile
from utils.data.batch_importer import CSVReader


class CSVTest(TestCase):

    def create_app(self):
        self.app = app.test_client()
        return app

    def csv_from_list(self, data):
        """
        Need to create a CSV file for upload purposes,
        will create a csv file and delete on terDown
        """
        self.file = parentdir + '/utils/data/test_csv.csv'
        with open(self.file, 'w+') as outfile:
            wr = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_ALL)
            wr.writerow(data)

    def setUp(self):
        Conn()

        data = [5, 'http://placekitten.com/g/500/500?user=3388',
                '2013-04-08', 'Blah', 'http://placekitten.com/g/500/500?user=1222',
                'Pinot Grigio', 'Lauren B.', 'Shelli K.', '2013-02-26']
        self.csv_from_list(data)
        CSVReader('test_csv.csv')

    def tearDown(self):
        #  Remove the test file
        os.remove(self.file)
        #  Clear table of data from setUp
        #  FIXME: need to delete from CSVImport with UUID
        OwnerBySitter.objects(sitter_id=3388).delete()
        OwnerNameByID.objects(owner_id=1222).delete()
        OwnerProfile.objects(id=1222).delete()
        RatingBySitter.objects(sitter_id=3388).delete()
        SitterByOwner.objects(owner_id=1222).delete()
        SitterNameByID.objects(sitter_id=3388).delete()
        SitterProfile.objects(id=3388).delete()

    #  FIXME: Need to search CSVImport table. Might not be necssary
    # def test_csv_import(self):
    #     q = CSVImport.objects.filter()

    def test_owner_by_sitter(self):
        q = OwnerBySitter.objects.filter(sitter_id=3388)
        match = q.get()
        self.assertEqual(match.owner_id, 1222)

if __name__ == '__main__':
    unittest.main()
