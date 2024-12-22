from unittest.mock import mock_open, patch

import pytest

from crud.libs.version import get_app_version


def test_valid_version():
    valid_versions = (
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
    )
    for version in valid_versions:
        with patch('builtins.open', mock_open(read_data=version)):
            assert get_app_version() == version


def test_invalid_version():
    invalid_versions = (
        '1.0',
        '1.0.0-',
        '1.0.0-01',
        '1.0.0+',
        '1.0.0-alpha..1',
        '1.0.0-alpha.01',
        '1.0.0.0',
    )
    for version in invalid_versions:
        with patch('builtins.open', mock_open(read_data=version)):
            with pytest.raises(ValueError):
                get_app_version()
