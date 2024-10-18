import re


def is_semantic_version_format(input_version: str) -> bool:
    '''
    Semantic Versioning 2.0 형식이 맞는지 검사하여 True/False로 리턴한다.
    형식: MAJOR.MINOR.PATCH-PRERELEASE+BUILD
    '''
    semver_pattern = r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)' \
                     r'(?:-((?:0|[1-9]\d*|[a-zA-Z-][0-9a-zA-Z-]*)' \
                     r'(?:\.(?:0|[1-9]\d*|[a-zA-Z-][0-9a-zA-Z-]*))*))?' \
                     r'(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$'
    return bool(re.match(semver_pattern, input_version))


def get_app_version() -> str:
    '''
    VERSION 파일에서 버전을 읽어와서 Semantic Versioning 2.0 형식이 맞는지 검사한다.
    잘못된 형식인 경우 ValueError가 raise 된다.
    '''

    with open('VERSION', 'r', encoding='utf-8') as f:
        version = f.read().strip()

    if not is_semantic_version_format(version):
        raise ValueError(f'Invalid version format: {version}')

    return version
