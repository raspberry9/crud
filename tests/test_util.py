from unittest.mock import mock_open, patch

import pytest

from crud.libs.version import get_app_version
from crud.libs.database import is_valid_database_url
from crud.libs.database import is_valid_sqlite_file_url


def test_valid_version():
    valid_versions = [
        '1.0.0',
        '0.1.0',
        '1.0.0-alpha',
        '1.0.0-alpha.1',
        '1.0.0-a.1',
        '1.0.0-a1',
        '1.0.0-beta',
        '1.0.0-beta.1',
        '1.0.0-b.1',
        '1.0.0-b1',
        '1.0.0-rc.1',
        '1.0.0-rc1',
        '1.0.0-post.1',
        '1.0.0-post1',
        '1.0.0+20130313144700',
        '1.0.0-beta+exp.sha.5114f85',
    ]
    for version in valid_versions:
        with patch("builtins.open", mock_open(read_data=version)):
            assert get_app_version() == version


def test_invalid_version():
    invalid_versions = [
        '1.0',
        '1.0.0-',
        '1.0.0-01',
        '1.0.0+',
        '1.0.0-alpha..1',
        '1.0.0-alpha.01',
        '1.0.0.0',
    ]
    for version in invalid_versions:
        with patch("builtins.open", mock_open(read_data=version)):
            with pytest.raises(ValueError):
                get_app_version()


def test_is_valid_database_url():
    valid_urls = [
        # "sqlite+aiosqlite:///./test.db",
        "postgresql+asyncpg://user:password@localhost:5432/mydatabase",
        "mysql+aiomysql://user:password@localhost/mydatabase",
        # "sqlite:///./test.db",
    ]
    invalid_urls = [
        "invalid_url",
        "postgresql://user@localhost:5432",
        "mysql://user:password@localhost",
        "sqlite://",
    ]

    for url in valid_urls:
        assert is_valid_database_url(url) == True, f'Failed for {url}'

    for url in invalid_urls:
        assert is_valid_database_url(url) == False, f'Failed for {url}'


def test_is_valid_sqlite_file_url():
    valid_urls = [
        "sqlite:///./test.db",
        "sqlite+aiosqlite:///./test.db",
        "sqlite:///path/to/database.db",
        "sqlite+aiosqlite:///path/to/database.db",
    ]
    invalid_urls = [
        "invalid_url",
        "sqlite://",
        "sqlite:/path/to/database.db",
        "sqlite+aiosqlite://path/to/database.db",
    ]

    for url in valid_urls:
        assert is_valid_sqlite_file_url(url) == True, f"Failed for {url}"

    for url in invalid_urls:
        assert is_valid_sqlite_file_url(url) == False, f"Failed for {url}"
