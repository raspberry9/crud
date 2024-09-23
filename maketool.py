"""
아래의 내용을 python 코드로 작성해줘.

이 스크립트는 Linux, MacOS, Windows OS 플랫폼에서 공통으로 Makefile 파일에서 간단하게 사용할 수 있는 cross platform makefile helper임
이 코드는 Python3.8 이상에서 사용할 수 있음

command라는 이름의 decorator로 command를 등록하면 쉽게 명령어를 추가할 수 있음
--help 명령어로 도움말을 출력할 수 있음
도움말에는 Usage와 각 커맨드의 간략한 설명이 표시됨

아래의 각 command를 실행할 때 뒤에 --help를 붙여서 설명과 입력이 필요한 required, optional argument를 알려줌
아래의 각 command 함수는 재사용 할 수 있도록 출력할 값을 return하고 함수 밖에서 그 내용을 출력한다.

사용법:

- GetOS 명령으로 현재 OS Platform을 출력함
$ python maketool2.py GetOS
Linux

- GetHash 명령으로 지정한 파일의 md5 hash 값을 보여줌
$ python maketool2.py GetHash <FILEPATH>
9a329afe837c5b80590e1385fbf8fca7
"""
import argparse
import sys
import platform
import hashlib

class ParsedArgs:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class CommandHandler:
    __commands__ = {}

    @classmethod
    def command(cls, func):
        cmd = func.__name__
        if cmd in cls.__commands__:
            raise ValueError(f'command {cmd} is duplicated')
        cls.__commands__[cmd] = func

        def deco(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f'ERROR: {e}', file=sys.stderr)
                sys.exit(1)

        return deco

    @classmethod
    def get_command_manual(cls, cmd):
        return f'Usage: python {sys.argv[0]} {cmd} [options]'

ch = CommandHandler()

@ch.command
def GetOS(args=None):
    """현재 OS 플랫폼을 출력합니다."""
    return platform.system()

@ch.command
def GetHash(args):
    """지정한 파일의 md5 해시 값을 출력합니다."""
    filepath = args.filepath
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Cross platform makefile helper')
    subparsers = parser.add_subparsers(dest='command', required=True)

    for cmd_name, cmd_func in ch.__commands__.items():
        cmd_parser = subparsers.add_parser(cmd_name, help=cmd_func.__doc__)
        if cmd_name == 'GetHash':
            cmd_parser.add_argument('filepath', type=str, help='파일 경로')
        cmd_parser.set_defaults(func=cmd_func)

    args = parser.parse_args()
    if 'func' in args:
        result = args.func(args)
        print(result)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
