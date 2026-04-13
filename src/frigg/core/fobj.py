from abc import ABC

from frigg.core.fid import FId


class FObj(ABC):
    _id: FId

    def __init__(self, namespace: str, name: str) -> None:
        self._id = FId(namespace, name)

    @property
    def id(self) -> FId:
        return self._id
