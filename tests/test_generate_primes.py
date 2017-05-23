from unittest import TestCase


class TestGenerate_primes(TestCase):
    def test_generate_primes(self):
        try:
            from build import generate_primes
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, generate_primes, None)
        self.assertRaises(TypeError, generate_primes, 98.6)
        self.assertEqual(generate_primes(20), [False, False, True,
                                                           True, False, True,
                                                           False, True, False,
                                                           False, False, True,
                                                           False, True, False,
                                                           False, False, True,
                                                           False, True])