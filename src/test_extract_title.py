import unittest
from extract_title import *

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown1 = "# Tolkien"
        markdown2 = "Tolkien"
        ex_header1 = extract_title(markdown1)
        self.assertEqual("Tolkien", ex_header1)
        with self.assertRaises(Exception):
            extract_title(markdown2)
        
