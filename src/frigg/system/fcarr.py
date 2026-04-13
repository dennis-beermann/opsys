from frigg.core.fobj import FObj

NAMESPACE = "crr"


class FCarr(FObj):
    def __init__(self, name: str) -> None:
        super().__init__(NAMESPACE, name)
