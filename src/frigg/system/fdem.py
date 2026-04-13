from frigg.core.fobj import FObj

NAMESPACE = "dem"


class FDem(FObj):
    def __init__(self, name: str) -> None:
        super().__init__(NAMESPACE, name)
