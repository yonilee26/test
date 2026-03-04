import argparse


def greet(name: str):
    print(f"Hello, {name}!")


def main():
    parser = argparse.ArgumentParser(
        prog="greet",
        description="A simple CLI tool that greets a user"
    )

    parser.add_argument(
        "name",
        help="Name of the person to greet"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="greet 1.0"
    )

    args = parser.parse_args()

    greet(args.name)


if __name__ == "__main__":
    main()