from __future__ import annotations

from typing import Generic, Iterator, Iterable, TypeVar

from frigg.core.fid import FId
from frigg.core.fobj import FObj

T = TypeVar("T", bound=FObj)


class FReg(Generic[T]):
    def __init__(self) -> None:
        self._items: dict[FId, T] = {}

    def ids(self) -> list[FId]:
        return list(self._items.keys())

    def add(self, item: T) -> None:
        if item.id in self._items:
            raise ValueError(f"FReg already contains item with id {item.id}")
        self._items[item.id] = item

    def get(self, id: FId) -> T | None:
        return self._items.get(id)

    def remove(self, id: FId) -> None:
        try:
            self._items.pop(id)
        except KeyError as ex:
            raise KeyError(f"FReg does not contain item with id {id}") from ex

    def has(self, id: FId) -> bool:
        return id in self._items

    def values(self) -> Iterable[T]:
        return self._items.values()

    def __iter__(self) -> Iterator[T]:
        return iter(self._items.values())

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, id: FId) -> bool:
        return id in self._items
