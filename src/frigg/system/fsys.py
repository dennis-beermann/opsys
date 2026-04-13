from frigg.core.fid import FId
from frigg.core.fobj import FObj
from frigg.core.freg import FReg
from frigg.system.fbound import FBound
from frigg.system.fdem import FDem
from frigg.system.fnode import FNode
from frigg.system.fcarr import FCarr

NAMESPACE = "sys"


class FSys(FObj):
    _id: FId
    nodes: FReg[FNode]
    carriers: FReg[FCarr]
    bounds: FReg[FBound]
    demands: FReg[FDem]

    def __init__(self, name: str) -> None:
        self._id = FId(NAMESPACE, name)
        self.nodes = FReg[FNode]()
        self.carriers = FReg[FCarr]()
        self.bounds = FReg[FBound]()
        self.demands = FReg[FDem]()

    @property
    def id(self) -> FId:
        return self._id
