def dict_filter_none(data: dict = None, /, **kwargs) -> dict:
    _dict = data or kwargs

    return {
        key: value
        for key, value in _dict.items()
        if value is not None
    }


def dict_filter_none_and_self(data: dict = None, /, **kwargs) -> dict:
    _data = data or kwargs
    if "self" in _data:
        _data.pop("self")

    return dict_filter_none(_data)
