import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test"""

    def test_first_last_name(self):
        """Test"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")


if __name__ == '__main__':
    unittest.main()
