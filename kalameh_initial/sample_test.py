# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import unittest
from source import words_check


class Kalameh_Bazi_Test(unittest.TestCase):

    def test_sample_1(self):
        self.assertDictEqual(words_check("""hEllO My FriEnDs!!!
thIS is A tEsT For your #p#r#o#b#l#e#m a"""),
                             {'Hello': 1, 'My': 1, 'Friends': 1, 'This': 1, 'Is': 1, 'A': 2, 'Test': 1, 'For': 1,
                              'Your': 1})

    def test_sample_2(self):
        self.assertDictEqual(words_check("""HeLLLO_O My________________FRIEND
HOW ARE YOUUUUU?___?
I Don'T KNow Y_O_U_R_N_A_M_E yet !!!!!!!!"""),
                             {'Hellloo': 1, 'How': 1, 'Are': 1, 'Youuuuu': 1, 'I': 1, 'Dont': 1, 'Know': 1,
                              'Yourname': 1, 'Yet': 1})


if __name__ == '__main__':
    unittest.main()
