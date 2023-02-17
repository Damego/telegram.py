from .const import URL


class Route:
    token: str

    def __init__(self, method: str, endpoint: str):
        self.method: str = method
        self.endpoint: str = endpoint

    @property
    def url(self) -> str:
        return f"{URL}{self.token}{self.endpoint}"
