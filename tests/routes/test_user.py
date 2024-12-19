import os
from unittest import mock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.exc import IntegrityError

from crud.controller.user import create_user
from crud.schemas.user import UserCreate

from crud.__main__ import app

client = TestClient(app)


def test_create_duplicated_user(db):
    user_to_create = UserCreate(name='myname', email='myemail@kormail.net')
    created_user = create_user(db, user_to_create)
    assert created_user.id == 1
    assert created_user.name == user_to_create.name
    with pytest.raises(IntegrityError):
        create_user(db, user_to_create)


@pytest.mark.parametrize('offset', [-1, 0, 1, 2, 999, 1024, 65535])
def test_get_users_offset_parameter(db, offset):
    # TODO: Implement this test case and also test for limit parameter
    pass
