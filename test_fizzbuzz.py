import unittest

from fizzbuzz import fizzbuzz_value, generate_sequence


class FizzBuzzTests(unittest.TestCase):
    def test_fizzbuzz_value_rules(self) -> None:
        self.assertEqual(fizzbuzz_value(1), "1")
        self.assertEqual(fizzbuzz_value(3), "Fizz")
        self.assertEqual(fizzbuzz_value(5), "Buzz")
        self.assertEqual(fizzbuzz_value(15), "FizzBuzz")

    def test_generate_sequence_defaults_to_one_hundred_values(self) -> None:
        sequence = generate_sequence()

        self.assertEqual(len(sequence), 100)
        self.assertEqual(sequence[:5], ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(sequence[14], "FizzBuzz")
        self.assertEqual(sequence[-1], "Buzz")


if __name__ == "__main__":
    unittest.main()
