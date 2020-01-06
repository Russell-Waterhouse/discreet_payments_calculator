from unittest import TestCase

import calculate_value


class Test(TestCase):

    def test_future_to_present(self):
        self.assertAlmostEqual(825.05, calculate_value.future_to_present(1000, 0.05, 10, 0.03), delta=0.01)

    def test_future_to_present_zero_values(self):
        self.assertAlmostEqual(0, calculate_value.future_to_present(0, 0.05, 10, 0), delta=0.01)
        self.assertAlmostEqual(1000, calculate_value.future_to_present(1000, 0.05, 0, 0), delta=0.01)
        self.assertAlmostEqual(1000, calculate_value.future_to_present(1000, 0, 10, 0), delta=0.01)

    def test_present_to_future(self):
        self.assertAlmostEqual(1000, calculate_value.present_to_future(825.05, 0.05, 10, 0.03), delta=0.01)

    def test_present_to_future_zero_values(self):
        self.assertAlmostEqual(0, calculate_value.present_to_future(0, 0.05, 10, 0), delta=0.01)
        self.assertAlmostEqual(613.91, calculate_value.present_to_future(613.91, 0, 10, 0), delta=0.01)
        self.assertAlmostEqual(613.91, calculate_value.present_to_future(613.91, 0.05, 0, 0), delta=0.01)
