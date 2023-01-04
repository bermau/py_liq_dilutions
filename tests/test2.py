import unittest
from liquid_dilutions import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.mater = Liquid("COVID")
        self.diluent = Liquid("Diluent")
        self.tube_as_cc = Aliquot(mater, 200, 154)
        self.tube_ct_mere = Aliquot(mater, 500, ct=20.5, unit_type='ct')

    def test_presentation(self):
        print(self.diluent)

    def test_04_preparer_dilution_de_ct_imposant_dilutions(self):
        print(f"\nSOLUTION DEPART {self.tube_ct_mere} \n")
        res = preparer(220, 35, self.tube_ct_mere, n_dil=3, lst_imposed_dil=[[100, 200], [150, 210]], comment=True)
        print()
        print(res)

    def test_06_preparer_dilution_de_ct(self):
        print(f"\nSOLUTION DEPART {self.tube_ct_mere} \n")
        res = preparer(200, 35, self.tube_ct_mere, comment=True)
        print()
        print(res)

    def test_08_dilution_ct_en_fille(self):
        print(self.tube_ct_mere)
        fille0 = diluer(self.tube_ct_mere, 10, volume_final=300, tag='la_fille', comment=True)
        print(fille0)

    def test_10_dilution_ct_par_defaut(self):
        print(self.tube_ct_mere)
        fille0 = diluer(self.tube_ct_mere, 10)
        print(fille0)

    def test_20_dilution(self):
        preparer(200, 15, self.tube_as_cc)

    def test_30_dilution(self):
        preparer(200, 15, self.tube_ct_mere, comment=True)

    # self.assertAlmostEqual(T.height_for_volume(3000), 38.20, 2)
    # self.assertAlmostEqual(T.height_for_volume(500), 6.37, 2)


if __name__ == '__main__':
    unittest.main()
