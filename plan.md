# Plan: Shift Fizz/Buzz To A New Pattern

## 1. Define the new pattern explicitly first
- Decide whether "range pattern" means:
  - Value intervals, for example Fizz for 10-20 and Buzz for 30-40.
  - Cyclic position ranges, for example in each block of 12 numbers: Fizz on positions 2-4 and Buzz on positions 8-9.
- Write 5-10 example inputs/outputs for the new behavior before coding.

## 2. Isolate rule evaluation behind a configurable rules object
- Refactor `fizzbuzz.py` so the decision logic is data-driven instead of hardcoded `3/5/15` checks.
- Add a small rule format, for example:
  - Divisibility mode: `{"label": "Fizz", "every": 3}`
  - Range mode: `{"label": "Fizz", "start": 10, "end": 20}`
  - Optional cyclic mode: `{"label": "Fizz", "cycle": 12, "from_pos": 2, "to_pos": 4}`

## 3. Update `fizzbuzz_value` signature to accept pattern config
- Keep current default behavior so existing callers still work.
- Example direction:
  - `fizzbuzz_value(number, rules=None)` where `rules` defaults to classic FizzBuzz.
- Preserve precedence handling (FizzBuzz when both conditions match).

## 4. Keep sequence generator compatible
- Extend `generate_sequence(limit=100, rules=None)` so the same custom pattern can be applied across the full output.
- Default path should still produce today's exact output for `limit=100`.

## 5. Expand tests to cover both old and new behavior
- Update `test_fizzbuzz.py`:
  - Keep all existing assertions for regression safety.
  - Add tests for the new range pattern:
    - Inside fizz range only.
    - Inside buzz range only.
    - Overlap range returns combined label (or your chosen precedence rule).
    - Outside ranges returns number string.
- Add one sequence-level test using a short limit and expected list snapshot.

## 6. Document how to switch patterns
- Update `README.md` with one example of classic mode and one example of the new range mode.
- Include expected sample output for clarity.

## 7. Optional hardening
- Add validation for invalid ranges (`start > end`, non-positive cycle, out-of-cycle positions).
- Raise `ValueError` with clear messages.

## Recommended minimal first implementation
- Implement interval ranges only first (simplest and closest to the request).
- Add cyclic ranges later if repeating patterns are needed instead of fixed absolute intervals.