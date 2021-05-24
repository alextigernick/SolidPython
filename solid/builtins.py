from typing import Tuple, Union, Sequence
from pathlib import Path

from .object_base import OpenSCADObject, IncludedOpenSCADObject
from .helpers import escpape_openscad_identifier
from .exp_extensions.part_hole import part, hole

#base data types -> why do we need them? What happened to the good ol' duck typing?
P2 = Tuple[float, float]
P3 = Tuple[float, float, float]
P4 = Tuple[float, float, float, float]
Vec3 = P3
Vec4 = P4
Vec34 = Union[Vec3, Vec4]
P3s = Sequence[P3]
P23 = Union[P2, P3]
Points = Sequence[P23]
Indexes = Union[Sequence[int], Sequence[Sequence[int]]]
ScadSize = Union[int, Sequence[float]]

#do we need this??? or is this some old unused stuff?
#Is it used in the public interface? git grep says it's unused internally -jeff
OpenSCADObjectPlus = Union[OpenSCADObject, Sequence[OpenSCADObject]]

# ====================
# = dynamic builtins =
# ====================
"""
    This block loads all the built in OpenSCAD functions (like circle, square,
    color, translate.....) from builtins.openscad file.
    I intentionally didn't use a *.scad file because it would be ignore through
    .gitignore und would be a pain to maintain (unless we remove *.scad from
    .gitignore, but that would cause a lot of generated files to show up while
    developing...). The only drawback is, that you have to setup your editor to
    also use OpenScad syntax highlighting for *.openscad files.
"""
OPENSCAD_BUILTINS_FILE = Path(__file__).absolute().parent / "builtins.openscad"

from .scad_import import use
builtins_symbols = use(OPENSCAD_BUILTINS_FILE, builtins=True)


# ========================
# = Cascading Operations =
# ========================
"""
    This is a "hack" to add cascading operations like:
        cube([10, 20, 30]).translate([-5, 0, 0])
    It simply takes every symbol (function or module name) and adds a wrapper
    function to the OpenSCADObject class. :D

    I really like this style and I don't see any reason why SolidPython should
    not support it. Are there any?
"""
def add_to_openSCADObject(name):
    def wrapper(self, *args, **kwargs):
        #retrieve the builtin from the local namespace
        builtin = globals()[name]
        #and return an instance of it with self as child
        return builtin(*args, **kwargs)(self)

    #set OpenSCADObject.{name} = wrapper
    #this means for example solidpython code like
    #   c.translate(...)
    #       will call the wrapper and will retrieve an instance of an translate
    #       node wrapped around c
    setattr(OpenSCADObject, name, wrapper)

cascading_builtins = ("union difference intersection intersection_for translate " +\
                      "scale rotate mirror resize color offset hull render " +\
                      "linear_extrude rotate_extrude projection surface").split(" ")

for b in cascading_builtins:
    add_to_openSCADObject(escpape_openscad_identifier(b))

# ================================
# = Modifier Convenience Methods =
# ================================
def debug(openscad_obj: OpenSCADObject) -> OpenSCADObject:
    return openscad_obj.debug()

def background(openscad_obj: OpenSCADObject) -> OpenSCADObject:
    return openscad_obj.background()

def root(openscad_obj: OpenSCADObject) -> OpenSCADObject:
    return openscad_obj.root()

def disable(openscad_obj: OpenSCADObject) -> OpenSCADObject:
    return openscad_obj.disable()

