import unittest
import converter


class ConverterTest(unittest.TestCase):
    def test_task(self):
        self.assertEqual(converter.json_to_html(),  # Here the function result is compared with the expected result.
                         ('<ul><li><span>Title #1</span><content><ul><li><p>Example 1</p><header>header 1</header>'
                          '</li></ul></content></li><li><div>div 1</div></li></ul>'))


if __name__ == '__main__':
    unittest.main()
