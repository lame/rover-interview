import csv
import os
import re

from dateutil import parser
from models.csv_import import CSVImport
from models.owner_by_sitter import OwnerBySitter
from models.owner_name_by_id import OwnerNameByID
from models.owner_profile import OwnerProfile
from models.sitter_by_owner import SitterByOwner
from models.sitter_name_by_id import SitterNameByID
from models.sitter_profile import SitterProfile
from models.connect_to_cluster import Conn


class CSVWalker:

    def __init__(self, infile=None):
        if infile is None:
            self.csv_walker('reviews.csv')
        else:
            self.csv_walker(infile)

    def csv_walker(self, file):
        Conn()
        with open(os.path.abspath(os.curdir + '/utils/data/' + file),
                  'r') as csvfile:
            next(csvfile)
            csv_reader = csv.reader(csvfile)

            """
            This for loop will fill out all of the tables,
            including the duplicate tables. Will create a
            data migration script at a later date. An overloaded
            save is another option in the CSVImport class
            but has a tendency to cause circular import problems
            as the codebase expands.
            """
            for row in csv_reader:

                #  TODO<Ryan>: This should be threaded off for every save async

                #  Populate csv_import table
                csv_import = CSVImport()
                csv_import.sitter_id = re.findall('(?<=\\=)(.*$)', row[1])[0]
                csv_import.rating = row[0]
                csv_import.sitter_image = row[1]
                csv_import.start_date = parser.parse(row[8])
                csv_import.end_date = parser.parse(row[2])
                csv_import.profile_text = row[3]
                csv_import.owner_image = row[4]
                csv_import.dogs = set(row[5].split('|'))
                csv_import.sitter = row[6]
                csv_import.owner = row[7]
                csv_import.owner_id = re.findall('(?<=\\=)(.*$)', row[4])[0]
                csv_import.save()

                owner_by_sitter = OwnerBySitter()
                owner_by_sitter.sitter_id = re.findall('(?<=\\=)(.*$)', row[1])[0]
                owner_by_sitter.start_date = parser.parse(row[8])
                owner_by_sitter.end_date = parser.parse(row[2])
                owner_by_sitter.owner_id = re.findall('(?<=\\=)(.*$)', row[4])[0]
                owner_by_sitter.save()

                owner_name_by_id = OwnerNameByID()
                owner_name_by_id.owner_name = row[7]
                owner_name_by_id.owner_id = re.findall('(?<=\\=)(.*$)', row[4])[0]
                owner_name_by_id.save()

                owner_profile = OwnerProfile()
                owner_profile.id = re.findall('(?<=\\=)(.*$)', row[4])[0]
                owner_profile.image = row[4]
                owner_profile.owner_review_text = row[3]
                owner_profile.dogs = set(row[5].split('|'))
                owner_profile.save()

                sitter_by_owner = SitterByOwner()
                sitter_by_owner.owner_id = re.findall('(?<=\\=)(.*$)', row[4])[0]
                sitter_by_owner.sitter_id = re.findall('(?<=\\=)(.*$)', row[1])[0]
                sitter_by_owner.start_date = parser.parse(row[8])
                sitter_by_owner.end_date = parser.parse(row[2])
                sitter_by_owner.dogs_handled = set(row[5].split('|'))
                sitter_by_owner.save()

                sitter_name_by_id = SitterNameByID()
                sitter_name_by_id.sitter_id = re.findall('(?<=\\=)(.*$)', row[1])[0]
                sitter_name_by_id.sitter_name = row[6]
                sitter_name_by_id.save()

                sitter_profile = SitterProfile()
                sitter_profile.id = re.findall('(?<=\\=)(.*$)', row[1])[0]
                sitter_profile.image = row[1]
                sitter_profile.owner_review_text = row[3]
                sitter_profile.save()

            print('Done with CSV import')
