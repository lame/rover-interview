import csv
import os
import re
import sys

from dateutil import parser

from models.csv_import import CSVImport
from models.owner_by_sitter import OwnerBySitter
from models.owner_id_by_name import OwnerIDByName
from models.owner_profile import OwnerProfile
from models.sitter_by_owner import SitterByOwner
from models.sitter_ import SitterIDByName
from models.sitter_profile import SitterProfile
from models.rating_by_sitter import RatingBySitter
from models.connect_to_cluster import Conn


class CSVReader:

    def __init__(self, infile=None):
        if infile is None:
            self.csv_walker('reviews.csv')
        else:
            self.csv_walker(infile)

    def csv_walker(self, file):
        Conn()
        #  FIXME: need to check that sys.path[0] works on other machines
        if os.path.isfile(os.getcwd() + '/utils/data/' + file):
            with open((os.getcwd() + '/utils/data/' + file),
                      'r') as csvfile:
                next(csvfile)
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    self.call_tables(row)

        elif os.path.isfile(os.path.abspath(sys.path[0] + '/utils/data/' + file)):
            with open(os.path.abspath(sys.path[0] + '/utils/data/' + file),
                      'r') as csvfile:
                next(csvfile)
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    self.call_tables(row)

    def call_tables(self, row):
        """
        This for loop will fill out all of the tables,
        including the duplicate tables. Will create a
        data migration script at a later date. An overloaded
        save is another option in the CSVImport class
        but has a tendency to cause circular import problems
        as the codebase expands.
        """
        self.populate_csv_import(row)
        self.populate_owner_by_sitter(row)
        self.populate_owner_id_by_name(row)
        self.populate_owner_profile(row)
        self.populate_sitter_by_owner(row)
        self.populate_sitter_id_by_name(row)
        self.populate_sitter_profile(row)
        self.populate_rating_by_sitter(row)

    def calculate_sitter_score(self, name):
        dist_letters = set()
        for letter in name:
            if letter.isalnum():
                dist_letters.add(letter.lower())

        return(5*(len(dist_letters)/26))

    def populate_csv_import(self, row):
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

    def populate_owner_by_sitter(self, row):
        owner_by_sitter = OwnerBySitter()
        owner_by_sitter.sitter_id = re.findall('(?<=\\=)(.*$)', row[1])[0]
        owner_by_sitter.start_date = parser.parse(row[8])
        owner_by_sitter.end_date = parser.parse(row[2])
        owner_by_sitter.owner_id = re.findall('(?<=\\=)(.*$)', row[4])[0]
        owner_by_sitter.save()

    def populate_owner_id_by_name(self, row):
        owner_name_by_id = OwnerIDByName()
        owner_name_by_id.owner_name = row[7]
        owner_name_by_id.owner_id = re.findall('(?<=\\=)(.*$)', row[4])[0]
        owner_name_by_id.save()

    def populate_owner_profile(self, row):
        owner_profile = OwnerProfile()
        owner_profile.id = re.findall('(?<=\\=)(.*$)', row[4])[0]
        owner_profile.name = row[7]
        owner_profile.image = row[4]
        owner_profile.owner_review_text = row[3]
        owner_profile.dogs = set(row[5].split('|'))
        owner_profile.save()

    def populate_sitter_by_owner(self, row):
        sitter_by_owner = SitterByOwner()
        sitter_by_owner.owner_id = re.findall('(?<=\\=)(.*$)', row[4])[0]
        sitter_by_owner.sitter_id = re.findall('(?<=\\=)(.*$)', row[1])[0]
        sitter_by_owner.start_date = parser.parse(row[8])
        sitter_by_owner.end_date = parser.parse(row[2])
        sitter_by_owner.dogs_handled = set(row[5].split('|'))
        sitter_by_owner.rating = row[0]
        sitter_by_owner.save()

    def populate_sitter_id_by_name(self, row):
        sitter_name_by_id = SitterIDByName()
        sitter_name_by_id.sitter_id = re.findall('(?<=\\=)(.*$)', row[1])[0]
        sitter_name_by_id.sitter_name = row[6]
        sitter_name_by_id.save()

    def populate_sitter_profile(self, row):
        sitter_profile = SitterProfile()
        sitter_profile.id = re.findall('(?<=\\=)(.*$)', row[1])[0]
        sitter_profile.name = row[6]
        sitter_profile.image = row[1]
        sitter_profile.owner_review_text = row[3]
        sitter_profile.rating = row[0]
        sitter_profile.score = self.calculate_sitter_score(row[6])
        sitter_profile.save()

    def populate_rating_by_sitter(self, row):
        rating_by_sitter = RatingBySitter()
        rating_by_sitter.sitter_id = re.findall('(?<=\\=)(.*$)', row[1])[0]
        rating_by_sitter.rating = row[0]
        rating_by_sitter.save()
