# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from pydantic import BaseModel


class CustomBaseModel(BaseModel):
    id: int
    created_at: str
    updated_at: str

    def dict(self, **kwargs):
        hidden_fields = set(
            attribute_name
            for attribute_name, model_field in self.__fields__.items()
            if model_field.field_info.extra.get("hidden") is True
        )
        kwargs.setdefault("exclude", hidden_fields)
        return super().dict(**kwargs)