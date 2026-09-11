# fizzbuzz-3

Basic FizzBuzz application for learning to code.

## Run

```bash
python fizzbuzz.py
```

## Test

```bash
python -m unittest test_fizzbuzz.py
```

## Configure A New Pattern

The app supports configurable rules for both classic divisibility and range-based
patterns.

### Classic behavior (default)

```python
from fizzbuzz import generate_sequence

print(generate_sequence(15))
```

### Suggested range pattern

```python
from fizzbuzz import SUGGESTED_RANGE_RULES, generate_sequence

print(generate_sequence(26, rules=SUGGESTED_RANGE_RULES))
```

Suggested parameters:
- Fizz: start 10, end 20
- Buzz: start 18, end 25

Example around the overlap:
- 17 -> Fizz
- 18 -> FizzBuzz
- 21 -> Buzz
