from crud.libs.logging import getLogger


def test_get_logger():
    logger = getLogger('test_logger')
    assert logger.name == 'test_logger'
