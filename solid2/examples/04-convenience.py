#! /usr/bin/env python

from solid2 import cube, sphere, rotate, down, forward

# the convenience module defines some convenience functions and "overloads" for
# some transformations and primitives to get a more convenient access to it.
# It provides for all OpenSCAD modules which need a "size" parameter to pass in
# single integers / floats (not wrapped in a list or tuple). In other words: you
# don't need to wrap sizes in [ and ]:
#
#       translate(10, 0, 0)(cube(1, 2, 3))
#
# The following transformations and modules are "overloaded":
#
#       translate, scale, resize, mirror, rotate, cube and square
#
# Furthermore it defines the following directions:
#
#       up, down, left, right, forward, fwd, back
#
# which all accept a single integer or float as parameter.

c = rotate(45, 45, 45)(
        down(5)(
            cube(10, 20, 30)
        )
    )

s = ~forward(5)(
        sphere(10)
    )

(c-s).save_as_scad()

# generates this scad code:
#
#    // Generated by ExpSolidPython
#
#    difference() {
#            rotate(a = [45, 45, 45]) {
#                    translate(v = [0, 0, -5]) {
#                            cube(size = [10, 20, 30]);
#                    };
#            };
#            #translate(v = [0, 5, 0]) {
#                    sphere(r = 10);
#            };
#    };

