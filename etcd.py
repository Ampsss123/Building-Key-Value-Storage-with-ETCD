import unittest
from unittest.mock import patch
from io import StringIO
import main  # Assuming your main script is named 'main.py'

class TestEtcdOperations(unittest.TestCase):
    def setUp(self):
        # Set up a StringIO object to capture printed output
        self.output = StringIO()

    def tearDown(self):
        # Clean up the StringIO object
        self.output.close()

    def test_put_key_value(self):
        # Test putting a key-value pair into etcd
        with patch('sys.stdout', new=self.output):
            result = main.put_key_value("/test/key", "value")
            self.assertEqual(result, "Key '/test/key' with value 'value' successfully added to etcd.\n")

    def test_get_value(self):
        # Test getting the value for a specific key from etcd
        with patch('sys.stdout', new=self.output):
            result = main.get_value("/test/key")
            self.assertEqual(result, "example_value\n")

    def test_delete_key(self):
        # Test deleting a key-value pair from etcd
        with patch('sys.stdout', new=self.output):
            result = main.delete_key("/test/key")
            self.assertEqual(result, "Key '/test/key' successfully deleted from etcd.\n")

    def test_list_keys(self):
        # Test listing all keys in etcd
        with patch('sys.stdout', new=self.output):
            result = main.list_keys()
            self.assertEqual(result, ["key1", "key2", "key3"])

if _name_ == '_main_':
    unittest.main()