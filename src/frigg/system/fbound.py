from frigg.core.fobj import FObj

NAMESPACE = "bnd"


class FBound(FObj):
    def __init__(self, name: str) -> None:
        super().__init__(NAMESPACE, name)
