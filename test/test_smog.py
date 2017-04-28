from unittest import TestCase, expectedFailure
from readability_score.calculatortest import CalculatorTest
from readability_score.calculators.smog import *

class SMOGTestCase(TestCase,CalculatorTest):
    def setUp(self):
        CalculatorTest.__init__(self, 20)
        self.calc = SMOG(self.text)

    def test_range_min_age(self):
        self.assertIn(self.calc.min_age, self.test_range, self.test_range_fail_text)

    @expectedFailure
    def test_exact_min_age(self):
        self.assertEqual(self.calc.min_age, self.min_age_test, "might break because of deps")