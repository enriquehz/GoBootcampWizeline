from copy import deepcopy
import unittest
import json

import app

BASE_URL = 'http://127.0.0.1:5000/api/v1.0/users'
BAD_ITEM_URL = '{}/50'.format(BASE_URL)
GOOD_ITEM_URL = '{}/1'.format(BASE_URL)

class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.backup_items = deepcopy(app.users)  # no references!
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all(self):
            response = self.app.get(BASE_URL)
            data = json.loads(response.get_data())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['users']), 6)

    def test_get_one(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['users'][0]['name'], 'Joe')

    def test_item_not_exist(self):
        response = self.app.get(BAD_ITEM_URL)
        self.assertEqual(response.status_code, 404)            

if __name__ == "__main__":
    unittest.main()       


