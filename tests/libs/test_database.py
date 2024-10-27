from crud.libs.database import is_valid_database_url, is_valid_sqlite_file_url


def test_is_valid_database_url():
    valid_urls = (
        "postgresql+asyncpg://user:password@localhost:5432/mydatabase",
        "mysql+aiomysql://user:password@localhost/mydatabase",
    )
    invalid_urls = (
        "invalid_url",
        "postgresql://user@localhost:5432",
        "mysql://user:password@localhost",
        "sqlite://",
    )

    for url in valid_urls:
        assert is_valid_database_url(url) == True, f'Failed for {url}'

    for url in invalid_urls:
        assert is_valid_database_url(url) == False, f'Failed for {url}'


def test_is_valid_sqlite_file_url():
    valid_urls = (
        "sqlite:///./test.db",
        "sqlite+aiosqlite:///./test.db",
        "sqlite:///path/to/database.db",
        "sqlite+aiosqlite:///path/to/database.db",
    )
    invalid_urls = (
        "invalid_url",
        "sqlite://",
        "sqlite:/path/to/database.db",
        "sqlite+aiosqlite://path/to/database.db",
    )

    for url in valid_urls:
        assert is_valid_sqlite_file_url(url) == True, f"Failed for {url}"

    for url in invalid_urls:
        assert is_valid_sqlite_file_url(url) == False, f"Failed for {url}"
