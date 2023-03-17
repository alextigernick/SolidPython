from ...core.object_base import OpenSCADObject, OpenSCADConstant
from ... import import_scad
from pathlib import Path

baseDir = Path(__file__).absolute().parent.parent.parent
importFile = baseDir / "libs" / "BOSL2" / "nema_steppers.scad"
_ = import_scad(f"{importFile}", use_not_include=False)

class nema11_stepper(OpenSCADObject):
    def __init__(self, h=None, shaft=None, shaft_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema11_stepper", {"h" : h, "shaft" : shaft, "shaft_len" : shaft_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema14_stepper(OpenSCADObject):
    def __init__(self, h=None, shaft=None, shaft_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema14_stepper", {"h" : h, "shaft" : shaft, "shaft_len" : shaft_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema17_stepper(OpenSCADObject):
    def __init__(self, h=None, shaft=None, shaft_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema17_stepper", {"h" : h, "shaft" : shaft, "shaft_len" : shaft_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema23_stepper(OpenSCADObject):
    def __init__(self, h=None, shaft=None, shaft_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema23_stepper", {"h" : h, "shaft" : shaft, "shaft_len" : shaft_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema34_stepper(OpenSCADObject):
    def __init__(self, h=None, shaft=None, shaft_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema34_stepper", {"h" : h, "shaft" : shaft, "shaft_len" : shaft_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema_mount_holes(OpenSCADObject):
    def __init__(self, size=None, depth=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema_mount_holes", {"size" : size, "depth" : depth, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema11_mount_holes(OpenSCADObject):
    def __init__(self, depth=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema11_mount_holes", {"depth" : depth, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema14_mount_holes(OpenSCADObject):
    def __init__(self, depth=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema14_mount_holes", {"depth" : depth, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema17_mount_holes(OpenSCADObject):
    def __init__(self, depth=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema17_mount_holes", {"depth" : depth, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema23_mount_holes(OpenSCADObject):
    def __init__(self, depth=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema23_mount_holes", {"depth" : depth, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema34_mount_holes(OpenSCADObject):
    def __init__(self, depth=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nema34_mount_holes", {"depth" : depth, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class nema_motor_width(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("nema_motor_width", {"size" : size, **kwargs})

class nema_motor_plinth_height(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("nema_motor_plinth_height", {"size" : size, **kwargs})

class nema_motor_plinth_diam(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("nema_motor_plinth_diam", {"size" : size, **kwargs})

class nema_motor_screw_spacing(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("nema_motor_screw_spacing", {"size" : size, **kwargs})

class nema_motor_screw_size(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("nema_motor_screw_size", {"size" : size, **kwargs})

class nema_motor_screw_depth(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("nema_motor_screw_depth", {"size" : size, **kwargs})

