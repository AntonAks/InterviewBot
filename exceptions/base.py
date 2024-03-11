from fastapi import status
from fastapi.encoders import jsonable_encoder
from typing import Any


class BaseError(Exception):
    status_code: int = 500
    default_message: str = "Undefined Error"
    details: str | None = None

    def __init__(self, *args, details=None):
        super().__init__(*args)
        self.details = details

    def __str__(self):
        return self.args[0] if self.args else self.default_message

    def to_json(self):
        as_json = {"message": str(self)}
        if self.details:
            as_json["details"] = jsonable_encoder(self.details)
        return as_json


class NotFoundError(BaseError):
    status_code = status.HTTP_404_NOT_FOUND
    default_message = "Not found"
