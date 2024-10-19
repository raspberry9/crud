# import os
# import sys
import logging
from typing import Optional


def getLogger(name: Optional[str] = None) -> logging.Logger:
    return logging.getLogger(name)
    # logger.setLevel(logging.DEBUG)
    # logger.addHandler(_file_handler())
    # logger.addHandler(_console_handler())
    # return logger

# def getLogger(name: Optional[str] = None) -> logging.Logger:
#     _set_fastapi_logformat()
#     _set_root_logformat()
#     logger = logging.getLogger(name)
#     if os.getenv('CURD_DEBUG', '0') == '1':
#         logger.setLevel(logging.DEBUG)
#     else:
#         logger.setLevel(logging.INFO)

#     logger.addHandler(_file_handler())
#     logger.addHandler(_console_handler())

#     return logger


# def _file_handler():
#     file_handler = logging.FileHandler('crud.log')
#     log_formatter = logging.Formatter("[%(asctime)s][%(levelname)s][%(name)s]: %(message)s")
#     file_handler.setFormatter(log_formatter)
#     return file_handler


# def _console_handler():
#     stream_handler = logging.StreamHandler(sys.stdout)
#     log_formatter = logging.Formatter("[%(asctime)s][%(levelname)s][%(name)s]: %(message)s")
#     stream_handler.setFormatter(log_formatter)
#     return stream_handler


# def _set_root_logformat():
#     fastapi_logger = logging.getLogger()
#     fastapi_logger.addHandler(_file_handler())
#     fastapi_logger.addHandler(_console_handler())
#     fastapi_logger.setLevel(logging.DEBUG)

# def _set_fastapi_logformat():
#     for logger_name in [None, 'root', 'uvicorn', 'uvicorn.error', 'uvicorn.access']:
#         fastapi_logger = logging.getLogger(logger_name)
#         fastapi_logger.addHandler(_file_handler())
#         fastapi_logger.addHandler(_console_handler())
#         fastapi_logger.setLevel(logging.DEBUG)
#     # fastapi_logger = logging.getLogger('uvicorn')
#     # fastapi_logger.addHandler(_file_handler())
#     # fastapi_logger.addHandler(_console_handler())
#     # fastapi_logger.setLevel(logging.DEBUG)


# # def _override_error_logformat():
# #     uvicorn_logger = logging.getLogger()
# #     uvicorn_logger.addHandler(_file_handler())
# #     uvicorn_logger.addHandler(_console_handler())
# #     uvicorn_logger.setLevel(logging.DEBUG)
