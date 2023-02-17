from typing import Type, Callable

from attrs import define


@define(kw_only=True)
class DictSerializerMixin:
    @classmethod
    def from_dict(cls, data: dict) -> "DictSerializerMixin":
        data = cls.process_dict(data)

        return cls(**data)

    @classmethod
    def process_dict(cls, data: dict) -> dict:
        return data


def convert_dataclass(converter: Type[DictSerializerMixin]) -> Callable[[dict | None], DictSerializerMixin | None]:
    def convert(value: dict | None):
        if value is None:
            return
        return converter.from_dict(value)

    return convert


def convert_list_dataclass(converter: Type[DictSerializerMixin]) -> Callable[[dict | None], list[DictSerializerMixin] | None]:
    def convert(value: list[dict] | None):
        if value is None:
            return
        return [converter.from_dict(item) for item in value]

    return convert
