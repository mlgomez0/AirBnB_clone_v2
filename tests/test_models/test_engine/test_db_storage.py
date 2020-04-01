#!/usr/bin/python3
import unittest
import MySQLdb
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class TestDbStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """set up for test"""

        cls.db = MySQLdb.connect(
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB'),
            host=os.getenv('HBNB_MYSQL_HOST')
        cls.cur = db.cursor()

    def test_query_all(self):
        expec = self.cur.execute("SELECT COUNT(id) FROM states ORDER BY id ASC")
        self.assertEqual(0, expec)
