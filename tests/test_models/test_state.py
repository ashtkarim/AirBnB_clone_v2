#!/usr/bin/python3
""" Unit test for State model """

import unittest
from models.state import State
from models.base_model import BaseModel

# Assuming BaseModel is correctly set up for SQLAlchemy
class TestState(unittest.TestCase):
    """ Test State model """

    def setUp(self):
        """ Set up the test environment """
        self.state = State()

    def tearDown(self):
        """ Tear down the test environment """
        pass # Add any necessary cleanup here

    def test_name_type(self):
        """ Test that the name attribute is a string """
        self.assertEqual(type(self.state.name), str)

    def test_name_value(self):
        """ Test that the name attribute has the correct value """
        self.state.name = "Test State"
        self.assertEqual(self.state.name, "Test State")

    def test_updated_at(self):
        """ Test that the updated_at attribute is correctly set """
        # Assuming State inherits from BaseModel and has an updated_at attribute
        self.assertIsNotNone(self.state.updated_at)

if __name__ == '__main__':
    unittest.main()
