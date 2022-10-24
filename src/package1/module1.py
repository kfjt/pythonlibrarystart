"""mylib package1 module1.
"""


def hello(name: str) -> str:
    """hello name.

    Args:
        name (str): your name

    Returns:
        str: greeting
    """
    return f"hello {name}"


def main():
    """main."""
    greeting = hello("app")
    print(greeting)


if __name__ == "__main__":
    main()
