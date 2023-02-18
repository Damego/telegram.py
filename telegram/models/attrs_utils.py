from typing import Type, Callable, TYPE_CHECKING, TypeVar

from attrs import define, field, Attribute

if TYPE_CHECKING:
    from ..http.client import HTTPClient

T = TypeVar("T")


@define(eq=False, order=False, hash=False, kw_only=True)
class DictSerializerMixin:
    @classmethod
    def from_dict(cls, data: dict):
        data = cls.process_dict(data)

        return cls(**data)

    @classmethod
    def from_list(cls, data: list[dict]):
        return [cls.from_dict(_) for _ in data]

    @classmethod
    def process_dict(cls, data: dict) -> dict:
        attr_names = [attr.name for attr in cls.__attrs_attrs__]
        return {key: value for key, value in data.items() if key in attr_names}


@define(eq=False, order=False, hash=False, kw_only=True)
class ClientSerializerMixin(DictSerializerMixin):
    http: "HTTPClient" = field(default=None)

    @classmethod
    def from_dict(cls, data: dict, http: "HTTPClient" = None):
        data = cls.process_dict(data, http)
        return cls(**data)

    @classmethod
    def from_list(cls, data: list[dict], http: "HTTPClient" = None):
        return [cls.from_dict(_, http=http) for _ in data]

    @classmethod
    def process_dict(cls, data: dict, http: "HTTPCLient") -> dict:
        for key, value in data.items():
            if isinstance(value, dict):
                value["http"] = http
            elif value and isinstance(value, list) and isinstance(value[0], dict):
                for val in value:
                    val["http"] = http
        return super().process_dict(data)


def convert_dataclass(converter: Type[T]) -> Callable[[dict | None], T | None]:
    def convert(value: dict | None):
        if value is None:
            return
        return converter.from_dict(value)

    return convert


def convert_list_dataclass(converter: Type[DictSerializerMixin]) -> Callable[[list[dict] | None], list[DictSerializerMixin] | None]:
    def convert(value: list[dict] | None):
        if value is None:
            return
        return [converter.from_dict(item) for item in value]

    return convert


def convert(converter):
    def _converter(value):
        if value is None:
            return
        return converter(value)

    return _converter