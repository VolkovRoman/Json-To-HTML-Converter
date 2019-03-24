import unittest
import converter


class ConverterTest(unittest.TestCase):
    def test_task(self):
        self.assertEqual(converter.json_to_html(),  # Here the function result is compared with the expected result.
                         '<h1>Title #1</h1><p>Hello World 1!</p><h1>Title #2</h1><p>Hello World 2!</p>')


if __name__ == '__main__':
    unittest.main()
