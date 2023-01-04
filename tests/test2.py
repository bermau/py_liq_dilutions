import unittest
import from  liquid_dilutions import *

class MyTestCase(unittest.TestCase):

    def test_a_cylinder_instance(self):
        T1 = Cylinder(50, 11)
        self.assertAlmostEqual(T1.height_for_volume(500), 5.26, 2)
        self.assertAlmostEqual(T1.height_for_volume(4000), 42.09, 2)

    def test_a_instance(self):
        part_sup2 = Cylinder(50, 10)
        T = TubeAs2Parts(part_sup2)
        self.assertAlmostEqual(T.height_for_volume(3000), 38.20, 2)
        self.assertAlmostEqual(T.height_for_volume(500), 6.37, 2)

    def test_tube_as_parts_from_cylinder_and_conical(self):
        my_top_part = Cylinder(50, 10)
        my_bottom_part = reagents.Conical(10, 10)
        T4 = TubeAs2Parts(my_top_part, my_bottom_part)
        T4.describe()
        self.assertAlmostEqual(T4.height_for_volume(100), 7.26, 2)
        self.assertAlmostEqual(T4.height_for_volume(200), 9.14, 2)
        self.assertAlmostEqual(T4.height_for_volume(1000), 15.63, 2)

    def test_apprixmation_tube(self):
        T = standard_5ml_tube_approximation
        self.assertAlmostEqual(T.height_for_volume(100), 1.08, 2)
        self.assertAlmostEqual(T.height_for_volume(1000), 10.82, 2)

    def test_for_rounded(self):
        T = RoundedBottomTube(50, 11)
        self.assertAlmostEqual(T.height_for_volume(500), 7.09, 2)
        self.assertAlmostEqual(T.height_for_volume(5000), 54.45, 2)

    def test_for_measured_test(self):
        from measured_values_for_tubes import measures_for_1_5ml_Eppendorf

        T = reagents.TubeAsMeasuredVolumes(measures_for_1_5ml_Eppendorf)
        print("volume max", T.max_volume)
        for vol in [100, 200, 300, 1000, 1490]:
            print(vol, T.height_for_volume(vol))
        self.assertAlmostEqual(T.height_for_volume(300), 16, 2)
        self.assertAlmostEqual(T.height_for_volume(1490), 32, 2)

if __name__ == '__main__':
    unittest.main()

