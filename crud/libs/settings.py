'''
Pydantic BaseSettings를 상속받아 환경변수를 읽어오는 기능을 추가한 BaseSettings 클래스
'''
import os
from typing import Dict

from pydantic.fields import PydanticUndefined
from pydantic_settings import BaseSettings as PydanticBaseSettings

from crud.libs.logging import getLogger

logger = getLogger(__name__)


class BaseSettings(PydanticBaseSettings):
    def __init__(self, *args, **kwargs):
        os_envs = self._get_envs_from_osenv()
        kwargs.update(os_envs)
        super().__init__(*args, **kwargs)
        self._set_envs(os_envs)

    def _get_envs_from_osenv(self) -> Dict[str, str]:
        envs = {}
        for field_name, field_val in self.model_fields.items():
            value = os.environ.get(field_name, '').strip()
            if value:
                envs[field_name] = os.environ[field_name]
            else:
                default_val = field_val.default
                if default_val is not PydanticUndefined:
                    envs[field_name] = default_val
        return envs

    def _set_envs(self, envs):
        for field_name, field_val in self.model_fields.items():
            value = envs.get(field_name)
            if value:
                setattr(self, field_name, value)
                logger.debug('Setting %s from env: %s', field_name, value)
            else:
                default_val = field_val.default
                if default_val is not PydanticUndefined:
                    setattr(self, field_name, default_val)
                    logger.debug('Setting %s from default: %s', field_name, value)
