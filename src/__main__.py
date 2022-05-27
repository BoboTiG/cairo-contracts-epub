import sys


def main() -> int:
    from .epub import make_it

    make_it()
    return 0


if __name__ == "__main__":
    sys.exit(main())
