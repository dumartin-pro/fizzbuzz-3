"""Basic FizzBuzz application."""


def fizzbuzz_value(number: int) -> str:
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def generate_sequence(limit: int = 100) -> list[str]:
    return [fizzbuzz_value(number) for number in range(1, limit + 1)]


def main() -> None:
    print("\n".join(generate_sequence()))


if __name__ == "__main__":
    main()
