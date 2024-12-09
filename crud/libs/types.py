from typing import Annotated

from pydantic import Field
from pydantic.networks import FileUrl, UrlConstraints

# NOTE: 현재 sqlite://file.db?mode=ro와 같은 query가 지원되지 않음. 확인이 필요함
SQLiteDsn = Annotated[FileUrl, UrlConstraints(allowed_schemes=['sqlite'])]

PortNumber = Annotated[int, Field(gt=0, le=65353)]
