import unittest
import converter


class ConverterTest(unittest.TestCase):
    def test_task(self):
        self.assertEqual(converter.json_to_html(),  # Here the function result is compared with the expected result.
                         ('<ul><li><h3>Title #1</h3><div>Hello World 1!</div></li>'
                         '<li><h3>Title #2</h3><div>Hello World 2!</div></li></ul>'))


if __name__ == '__main__':
    unittest.main()
