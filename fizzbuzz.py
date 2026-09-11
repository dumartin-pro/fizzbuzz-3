"""Basic FizzBuzz application."""

from typing import TypedDict


class FizzBuzzRule(TypedDict, total=False):
    label: str
    every: int
    start: int
    end: int


DEFAULT_RULES: list[FizzBuzzRule] = [
    {"label": "Fizz", "every": 3},
    {"label": "Buzz", "every": 5},
]

SUGGESTED_RANGE_RULES: list[FizzBuzzRule] = [
    {"label": "Fizz", "start": 10, "end": 20},
    {"label": "Buzz", "start": 18, "end": 25},
]


def _validate_rules(rules: list[FizzBuzzRule]) -> None:
    for rule in rules:
        label = rule.get("label")
        if not label:
            raise ValueError("Each rule must include a non-empty 'label'.")

        has_every = "every" in rule
        has_range = "start" in rule or "end" in rule

        if has_every and has_range:
            raise ValueError(
                "A rule must use either 'every' or 'start'/'end', not both."
            )

        if has_every:
            every = rule["every"]
            if every <= 0:
                raise ValueError("'every' must be a positive integer.")
            continue

        if "start" not in rule or "end" not in rule:
            raise ValueError("Range rules must include both 'start' and 'end'.")

        if rule["start"] > rule["end"]:
            raise ValueError("Range rules must satisfy start <= end.")


def _matches_rule(number: int, rule: FizzBuzzRule) -> bool:
    if "every" in rule:
        return number % rule["every"] == 0

    return rule["start"] <= number <= rule["end"]


def fizzbuzz_value(number: int, rules: list[FizzBuzzRule] | None = None) -> str:
    active_rules = rules if rules is not None else DEFAULT_RULES
    _validate_rules(active_rules)

    matches = [rule["label"] for rule in active_rules if _matches_rule(number, rule)]
    if matches:
        return "".join(matches)

    return str(number)


def generate_sequence(
    limit: int = 100, rules: list[FizzBuzzRule] | None = None
) -> list[str]:
    return [fizzbuzz_value(number, rules=rules) for number in range(1, limit + 1)]


def main() -> None:
    print("\n".join(generate_sequence()))


if __name__ == "__main__":
    main()
