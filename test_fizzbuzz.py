import unittest

from fizzbuzz import (
    DEFAULT_RULES,
    SUGGESTED_RANGE_RULES,
    fizzbuzz_value,
    generate_sequence,
)


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

    def test_fizzbuzz_value_supports_suggested_range_rules(self) -> None:
        self.assertEqual(fizzbuzz_value(9, rules=SUGGESTED_RANGE_RULES), "9")
        self.assertEqual(fizzbuzz_value(10, rules=SUGGESTED_RANGE_RULES), "Fizz")
        self.assertEqual(fizzbuzz_value(18, rules=SUGGESTED_RANGE_RULES), "FizzBuzz")
        self.assertEqual(fizzbuzz_value(22, rules=SUGGESTED_RANGE_RULES), "Buzz")
        self.assertEqual(fizzbuzz_value(26, rules=SUGGESTED_RANGE_RULES), "26")

    def test_generate_sequence_supports_suggested_range_rules(self) -> None:
        sequence = generate_sequence(limit=26, rules=SUGGESTED_RANGE_RULES)

        self.assertEqual(len(sequence), 26)
        self.assertEqual(sequence[8], "9")
        self.assertEqual(sequence[9], "Fizz")
        self.assertEqual(sequence[17], "FizzBuzz")
        self.assertEqual(sequence[21], "Buzz")
        self.assertEqual(sequence[-1], "26")

    def test_invalid_rules_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            fizzbuzz_value(1, rules=[{"label": "Fizz", "every": 0}])

        with self.assertRaises(ValueError):
            fizzbuzz_value(1, rules=[{"label": "Buzz", "start": 20, "end": 10}])

        with self.assertRaises(ValueError):
            fizzbuzz_value(1, rules=[{"label": "Fizz", "start": 10}])

    def test_default_rules_constant_matches_classic_behavior(self) -> None:
        self.assertEqual(fizzbuzz_value(3, rules=DEFAULT_RULES), "Fizz")
        self.assertEqual(fizzbuzz_value(5, rules=DEFAULT_RULES), "Buzz")
        self.assertEqual(fizzbuzz_value(15, rules=DEFAULT_RULES), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
