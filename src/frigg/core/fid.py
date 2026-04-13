from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FId:
    namespace: str
    name: str

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("FId 'name' property empty")
        if not self.namespace:
            raise ValueError("FId 'namespace' property empty")

    def __str__(self) -> str:
        return self.id

    @property
    def id(self) -> str:
        return self.namespace + "_" + self.name
