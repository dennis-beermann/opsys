from frigg.core.fobj import FObj

NAMESPACE = "nod"


class FNode(FObj):
    def __init__(self, name: str) -> None:
        super().__init__(NAMESPACE, name)
