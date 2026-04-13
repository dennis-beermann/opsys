from frigg import FSys, FNode, FBound, FCarr, FDem

sys = FSys("example")
sys.nodes.add(FNode("n1"))
sys.carriers.add(FCarr("c1"))
sys.bounds.add(FBound("b1"))
sys.demands.add(FDem("d1"))
