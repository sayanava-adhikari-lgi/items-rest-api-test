
from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)
            self.assertIsNone(item.find_by_name('test'))
            item.save_to_db()
            self.assertIsNotNone(item.find_by_name('test'))
            item.delete_from_db()
            self.assertIsNone(item.find_by_name('test'))
