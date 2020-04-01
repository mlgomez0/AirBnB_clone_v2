#!/usr/bin/python3
import unittest
import MySQLdb
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import os


class TestDbStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User(email="gh@hotmail.com", password="pwdyes")
        cls.user.save()
        cls.db = MySQLdb.connect(
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB'),
            host=os.getenv('HBNB_MYSQL_HOST')
        cls.cur = db.cursor()

    def test_query_new(self):
        count_elem = cur.execute("SELECT COUNT(name) FROM states")
        state_c = State(name="California")
        state_c.save()
        count_new_elem = cur.execute("SELECT COUNT(name) FROM states")
        self.assertGreater(count_new_elem, count_elem)

