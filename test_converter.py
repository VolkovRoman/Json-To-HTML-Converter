import unittest
import converter


class ConverterTest(unittest.TestCase):
    def test_task(self):
        self.assertEqual(converter.json_to_html(),  # Here the function result is compared with the expected result.
                         '<h3>Title #1</h3><div>Hello World 1!</div>')


if __name__ == '__main__':
    unittest.main()
