import sys


def main():
    try:
        print('hello, world!')
        return 0
    except:
        return 1


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
