import sys
from enum import IntEnum


class ExitCode(IntEnum):
    SUCCESS = 0
    ERROR = 1


def main() -> ExitCode:
    try:
        print('hello, world!')
        return ExitCode.SUCCESS
    except:
        return ExitCode.ERROR


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
