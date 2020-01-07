from unittest import TestCase

import calculate_value


class Test(TestCase):
    def test_future_to_present(self):
        self.assertAlmostEqual(825.05, calculate_value.future_to_present(1000, 0.05, 10, 0.03), delta=0.01)

    def test_future_to_present_zero_values(self):
        self.assertAlmostEqual(0, calculate_value.future_to_present(0, 0.05, 10, 0), delta=0.01)
        self.assertAlmostEqual(1000, calculate_value.future_to_present(1000, 0.05, 0, 0), delta=0.01)
        self.assertAlmostEqual(1000, calculate_value.future_to_present(1000, 0, 10, 0), delta=0.01)

    def test_get_real_interest_rate(self):
        self.assertEqual(0, calculate_value.get_real_interest_rate(0.03, 0.03))
        self.assertEqual(0.08, calculate_value.get_real_interest_rate(0, 0.08))
        self.assertAlmostEqual(-0.055, calculate_value.get_real_interest_rate(0.08, 0.02), delta=0.01)

    def test_present_to_future(self):
        self.assertAlmostEqual(1000, calculate_value.present_to_future(825.05, 0.05, 10, 0.03), delta=0.01)

    def test_present_to_future_zero_values(self):
        self.assertAlmostEqual(0, calculate_value.present_to_future(0, 0.05, 10, 0), delta=0.01)
        self.assertAlmostEqual(613.91, calculate_value.present_to_future(613.91, 0, 10, 0), delta=0.01)
        self.assertAlmostEqual(613.91, calculate_value.present_to_future(613.91, 0.05, 0, 0), delta=0.01)

    def test_annuity_to_future(self):
        self.assertAlmostEqual(40710.0422, calculate_value.annuity_to_future(5000, 0.05, 7, 0), delta=0.01)

    def test_future_to_annuity(self):
        self.assertAlmostEqual(614.099, calculate_value.future_to_annuity(5000, 0.05, 7, 0), delta=0.01)

    def test_annuity_to_present(self):
        self.assertAlmostEqual(1000, calculate_value.annuity_to_present(263.797, 0.10, 5, 0), delta=0.01)
        self.assertAlmostEqual(5000, calculate_value.annuity_to_present(864.099, 0.05, 7, 0), delta=0.01)
        self.assertAlmostEqual(28931.8669, calculate_value.annuity_to_present(5000, 0.05, 7, 0), delta=0.01)

    def test_present_to_annuity(self):
        self.assertAlmostEqual(263.797, calculate_value.present_to_annuity(1000, 0.10, 5, 0.00), delta=0.01)
        self.assertAlmostEqual(864.099, calculate_value.present_to_annuity(5000, 0.05, 7, 0.00), delta=0.01)
