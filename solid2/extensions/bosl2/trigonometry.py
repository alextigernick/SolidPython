from ...core.object_base import OpenSCADObject, OpenSCADConstant
from ... import import_scad
from pathlib import Path

baseDir = Path(__file__).absolute().parent.parent.parent
importFile = baseDir / "libs" / "BOSL2" / "trigonometry.scad"
_ = import_scad(f"{importFile}", use_not_include=False)

class law_of_cosines(OpenSCADObject):
    def __init__(self, a=None, b=None, c=None, C=None, **kwargs):
       super().__init__("law_of_cosines", {"a" : a, "b" : b, "c" : c, "C" : C, **kwargs})

class law_of_sines(OpenSCADObject):
    def __init__(self, a=None, A=None, b=None, B=None, **kwargs):
       super().__init__("law_of_sines", {"a" : a, "A" : A, "b" : b, "B" : B, **kwargs})

class hyp_opp_to_adj(OpenSCADObject):
    def __init__(self, hyp=None, opp=None, **kwargs):
       super().__init__("hyp_opp_to_adj", {"hyp" : hyp, "opp" : opp, **kwargs})

class opp_hyp_to_adj(OpenSCADObject):
    def __init__(self, opp=None, hyp=None, **kwargs):
       super().__init__("opp_hyp_to_adj", {"opp" : opp, "hyp" : hyp, **kwargs})

class hyp_ang_to_adj(OpenSCADObject):
    def __init__(self, hyp=None, ang=None, **kwargs):
       super().__init__("hyp_ang_to_adj", {"hyp" : hyp, "ang" : ang, **kwargs})

class ang_hyp_to_adj(OpenSCADObject):
    def __init__(self, ang=None, hyp=None, **kwargs):
       super().__init__("ang_hyp_to_adj", {"ang" : ang, "hyp" : hyp, **kwargs})

class opp_ang_to_adj(OpenSCADObject):
    def __init__(self, opp=None, ang=None, **kwargs):
       super().__init__("opp_ang_to_adj", {"opp" : opp, "ang" : ang, **kwargs})

class ang_opp_to_adj(OpenSCADObject):
    def __init__(self, ang=None, opp=None, **kwargs):
       super().__init__("ang_opp_to_adj", {"ang" : ang, "opp" : opp, **kwargs})

class hyp_adj_to_opp(OpenSCADObject):
    def __init__(self, hyp=None, adj=None, **kwargs):
       super().__init__("hyp_adj_to_opp", {"hyp" : hyp, "adj" : adj, **kwargs})

class adj_hyp_to_opp(OpenSCADObject):
    def __init__(self, adj=None, hyp=None, **kwargs):
       super().__init__("adj_hyp_to_opp", {"adj" : adj, "hyp" : hyp, **kwargs})

class hyp_ang_to_opp(OpenSCADObject):
    def __init__(self, hyp=None, ang=None, **kwargs):
       super().__init__("hyp_ang_to_opp", {"hyp" : hyp, "ang" : ang, **kwargs})

class ang_hyp_to_opp(OpenSCADObject):
    def __init__(self, ang=None, hyp=None, **kwargs):
       super().__init__("ang_hyp_to_opp", {"ang" : ang, "hyp" : hyp, **kwargs})

class adj_ang_to_opp(OpenSCADObject):
    def __init__(self, adj=None, ang=None, **kwargs):
       super().__init__("adj_ang_to_opp", {"adj" : adj, "ang" : ang, **kwargs})

class ang_adj_to_opp(OpenSCADObject):
    def __init__(self, ang=None, adj=None, **kwargs):
       super().__init__("ang_adj_to_opp", {"ang" : ang, "adj" : adj, **kwargs})

class adj_opp_to_hyp(OpenSCADObject):
    def __init__(self, adj=None, opp=None, **kwargs):
       super().__init__("adj_opp_to_hyp", {"adj" : adj, "opp" : opp, **kwargs})

class opp_adj_to_hyp(OpenSCADObject):
    def __init__(self, opp=None, adj=None, **kwargs):
       super().__init__("opp_adj_to_hyp", {"opp" : opp, "adj" : adj, **kwargs})

class adj_ang_to_hyp(OpenSCADObject):
    def __init__(self, adj=None, ang=None, **kwargs):
       super().__init__("adj_ang_to_hyp", {"adj" : adj, "ang" : ang, **kwargs})

class ang_adj_to_hyp(OpenSCADObject):
    def __init__(self, ang=None, adj=None, **kwargs):
       super().__init__("ang_adj_to_hyp", {"ang" : ang, "adj" : adj, **kwargs})

class opp_ang_to_hyp(OpenSCADObject):
    def __init__(self, opp=None, ang=None, **kwargs):
       super().__init__("opp_ang_to_hyp", {"opp" : opp, "ang" : ang, **kwargs})

class ang_opp_to_hyp(OpenSCADObject):
    def __init__(self, ang=None, opp=None, **kwargs):
       super().__init__("ang_opp_to_hyp", {"ang" : ang, "opp" : opp, **kwargs})

class hyp_adj_to_ang(OpenSCADObject):
    def __init__(self, hyp=None, adj=None, **kwargs):
       super().__init__("hyp_adj_to_ang", {"hyp" : hyp, "adj" : adj, **kwargs})

class adj_hyp_to_ang(OpenSCADObject):
    def __init__(self, adj=None, hyp=None, **kwargs):
       super().__init__("adj_hyp_to_ang", {"adj" : adj, "hyp" : hyp, **kwargs})

class hyp_opp_to_ang(OpenSCADObject):
    def __init__(self, hyp=None, opp=None, **kwargs):
       super().__init__("hyp_opp_to_ang", {"hyp" : hyp, "opp" : opp, **kwargs})

class opp_hyp_to_ang(OpenSCADObject):
    def __init__(self, opp=None, hyp=None, **kwargs):
       super().__init__("opp_hyp_to_ang", {"opp" : opp, "hyp" : hyp, **kwargs})

class adj_opp_to_ang(OpenSCADObject):
    def __init__(self, adj=None, opp=None, **kwargs):
       super().__init__("adj_opp_to_ang", {"adj" : adj, "opp" : opp, **kwargs})

class opp_adj_to_ang(OpenSCADObject):
    def __init__(self, opp=None, adj=None, **kwargs):
       super().__init__("opp_adj_to_ang", {"opp" : opp, "adj" : adj, **kwargs})

