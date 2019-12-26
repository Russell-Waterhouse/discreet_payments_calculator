from unittest import TestCase
import calculate_value


class Test(TestCase):
    def test_future_to_present(self):
        self.assertAlmostEqual(613.91, calculate_value.future_to_present(1000, 0.05, 10), delta=0.01)

    def test_present_to_future(self):
        self.assertAlmostEqual(1000, calculate_value.present_to_future(613.91, 0.05, 10), delta=0.01)