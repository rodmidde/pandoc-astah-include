import unittest

from astah import get_filepaths_by_index, astah
from pandocfilters import Para, Image


class AstahTests(unittest.TestCase):

    def test_get_filepaths_by_index(self):
        self.assertEqual(get_filepaths_by_index(".", "pdf", 0), "./astah.pdf")

    def test_astah(self):
        keyvals = [[u'file', u'designs/Sample.asta'],
                   [u'caption', u'this is the caption'],
                   [u'index', u'1'],
                   [u'format', u'png']]
        value = [["", ["astah"], keyvals], ""]

        para = astah('CodeBlock', value, "", [])
        self.assertEqual(para, Para([Image(["", [], [[u'file', u'designs/Sample.asta'],
                                                     [u'index', u'1'],
                                                     [u'format', u'png']]], [{'c': u'this is the caption', 't': 'Str'}],
                                           ['astah-generated-files/Sample/DataFlow/00.Withdrawal '
                                            'service of saving account.png',
                                            'fig:'])]))

if __name__ == '__main__':
    unittest.main()
