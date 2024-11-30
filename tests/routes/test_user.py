import pytest

from sqlalchemy.exc import IntegrityError

from crud.controller.user import create_user
# from crud.models import get_db
from crud.schemas.user import UserCreate

#from tests.conftest import db


def test_create_duplicated_user(db):
    # db = get_db()
    user_to_create = UserCreate(name='myname', email='myemail@kormail.net')
    created_user = create_user(db, user_to_create)
    assert created_user.id == 0
    assert created_user.name == user_to_create.name
    with pytest.raises(IntegrityError):
        create_user(db, user_to_create)
