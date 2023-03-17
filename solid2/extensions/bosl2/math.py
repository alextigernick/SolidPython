from ...core.object_base import OpenSCADObject, OpenSCADConstant
from ... import import_scad
from pathlib import Path

baseDir = Path(__file__).absolute().parent.parent.parent
importFile = baseDir / "libs" / "BOSL2" / "math.scad"
_ = import_scad(f"{importFile}", use_not_include=False)

PHI = OpenSCADConstant('PHI')
EPSILON = OpenSCADConstant('EPSILON')
INF = OpenSCADConstant('INF')
NAN = OpenSCADConstant('NAN')
class count(OpenSCADObject):
    def __init__(self, n=None, s=None, step=None, reverse=None, **kwargs):
       super().__init__("count", {"n" : n, "s" : s, "step" : step, "reverse" : reverse, **kwargs})

class lerp(OpenSCADObject):
    def __init__(self, a=None, b=None, u=None, **kwargs):
       super().__init__("lerp", {"a" : a, "b" : b, "u" : u, **kwargs})

class lerpn(OpenSCADObject):
    def __init__(self, a=None, b=None, n=None, endpoint=None, **kwargs):
       super().__init__("lerpn", {"a" : a, "b" : b, "n" : n, "endpoint" : endpoint, **kwargs})

class sqr(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("sqr", {"x" : x, **kwargs})

class log2(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("log2", {"x" : x, **kwargs})

class hypot(OpenSCADObject):
    def __init__(self, x=None, y=None, z=None, **kwargs):
       super().__init__("hypot", {"x" : x, "y" : y, "z" : z, **kwargs})

class factorial(OpenSCADObject):
    def __init__(self, n=None, d=None, **kwargs):
       super().__init__("factorial", {"n" : n, "d" : d, **kwargs})

class binomial(OpenSCADObject):
    def __init__(self, n=None, **kwargs):
       super().__init__("binomial", {"n" : n, **kwargs})

class binomial_coefficient(OpenSCADObject):
    def __init__(self, n=None, k=None, **kwargs):
       super().__init__("binomial_coefficient", {"n" : n, "k" : k, **kwargs})

class gcd(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("gcd", {"a" : a, "b" : b, **kwargs})

class _lcm(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("_lcm", {"a" : a, "b" : b, **kwargs})

class _lcmlist(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("_lcmlist", {"a" : a, **kwargs})

class lcm(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("lcm", {"a" : a, "b" : b, **kwargs})

class sinh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("sinh", {"x" : x, **kwargs})

class cosh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("cosh", {"x" : x, **kwargs})

class tanh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("tanh", {"x" : x, **kwargs})

class asinh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("asinh", {"x" : x, **kwargs})

class acosh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("acosh", {"x" : x, **kwargs})

class atanh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("atanh", {"x" : x, **kwargs})

class quant(OpenSCADObject):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("quant", {"x" : x, "y" : y, **kwargs})

class quantdn(OpenSCADObject):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("quantdn", {"x" : x, "y" : y, **kwargs})

class quantup(OpenSCADObject):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("quantup", {"x" : x, "y" : y, **kwargs})

class constrain(OpenSCADObject):
    def __init__(self, v=None, minval=None, maxval=None, **kwargs):
       super().__init__("constrain", {"v" : v, "minval" : minval, "maxval" : maxval, **kwargs})

class posmod(OpenSCADObject):
    def __init__(self, x=None, m=None, **kwargs):
       super().__init__("posmod", {"x" : x, "m" : m, **kwargs})

class modang(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("modang", {"x" : x, **kwargs})

class sum(OpenSCADObject):
    def __init__(self, v=None, dflt=None, **kwargs):
       super().__init__("sum", {"v" : v, "dflt" : dflt, **kwargs})

class _sum(OpenSCADObject):
    def __init__(self, v=None, _total=None, _i=None, **kwargs):
       super().__init__("_sum", {"v" : v, "_total" : _total, "_i" : _i, **kwargs})

class mean(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("mean", {"v" : v, **kwargs})

class median(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("median", {"v" : v, **kwargs})

class deltas(OpenSCADObject):
    def __init__(self, v=None, wrap=None, **kwargs):
       super().__init__("deltas", {"v" : v, "wrap" : wrap, **kwargs})

class cumsum(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("cumsum", {"v" : v, **kwargs})

class _cumsum(OpenSCADObject):
    def __init__(self, v=None, _i=None, _acc=None, **kwargs):
       super().__init__("_cumsum", {"v" : v, "_i" : _i, "_acc" : _acc, **kwargs})

class product(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("product", {"v" : v, **kwargs})

class _product(OpenSCADObject):
    def __init__(self, v=None, i=None, _tot=None, **kwargs):
       super().__init__("_product", {"v" : v, "i" : i, "_tot" : _tot, **kwargs})

class cumprod(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("cumprod", {"list" : list, **kwargs})

class _cumprod(OpenSCADObject):
    def __init__(self, v=None, _i=None, _acc=None, **kwargs):
       super().__init__("_cumprod", {"v" : v, "_i" : _i, "_acc" : _acc, **kwargs})

class _cumprod_vec(OpenSCADObject):
    def __init__(self, v=None, _i=None, _acc=None, **kwargs):
       super().__init__("_cumprod_vec", {"v" : v, "_i" : _i, "_acc" : _acc, **kwargs})

class convolve(OpenSCADObject):
    def __init__(self, p=None, q=None, **kwargs):
       super().__init__("convolve", {"p" : p, "q" : q, **kwargs})

class sum_of_sines(OpenSCADObject):
    def __init__(self, a=None, sines=None, **kwargs):
       super().__init__("sum_of_sines", {"a" : a, "sines" : sines, **kwargs})

class rand_int(OpenSCADObject):
    def __init__(self, minval=None, maxval=None, n=None, seed=None, **kwargs):
       super().__init__("rand_int", {"minval" : minval, "maxval" : maxval, "n" : n, "seed" : seed, **kwargs})

class random_points(OpenSCADObject):
    def __init__(self, n=None, dim=None, scale=None, seed=None, **kwargs):
       super().__init__("random_points", {"n" : n, "dim" : dim, "scale" : scale, "seed" : seed, **kwargs})

class gaussian_rands(OpenSCADObject):
    def __init__(self, n=None, mean=None, cov=None, seed=None, **kwargs):
       super().__init__("gaussian_rands", {"n" : n, "mean" : mean, "cov" : cov, "seed" : seed, **kwargs})

class exponential_rands(OpenSCADObject):
    def __init__(self, n=None, _lambda=None, seed=None, **kwargs):
       super().__init__("exponential_rands", {"n" : n, "_lambda" : _lambda, "seed" : seed, **kwargs})

class spherical_random_points(OpenSCADObject):
    def __init__(self, n=None, radius=None, seed=None, **kwargs):
       super().__init__("spherical_random_points", {"n" : n, "radius" : radius, "seed" : seed, **kwargs})

class random_polygon(OpenSCADObject):
    def __init__(self, n=None, size=None, seed=None, **kwargs):
       super().__init__("random_polygon", {"n" : n, "size" : size, "seed" : seed, **kwargs})

class deriv(OpenSCADObject):
    def __init__(self, data=None, h=None, closed=None, **kwargs):
       super().__init__("deriv", {"data" : data, "h" : h, "closed" : closed, **kwargs})

class _dnu_calc(OpenSCADObject):
    def __init__(self, f1=None, fc=None, f2=None, h1=None, h2=None, **kwargs):
       super().__init__("_dnu_calc", {"f1" : f1, "fc" : fc, "f2" : f2, "h1" : h1, "h2" : h2, **kwargs})

class _deriv_nonuniform(OpenSCADObject):
    def __init__(self, data=None, h=None, closed=None, **kwargs):
       super().__init__("_deriv_nonuniform", {"data" : data, "h" : h, "closed" : closed, **kwargs})

class deriv2(OpenSCADObject):
    def __init__(self, data=None, h=None, closed=None, **kwargs):
       super().__init__("deriv2", {"data" : data, "h" : h, "closed" : closed, **kwargs})

class deriv3(OpenSCADObject):
    def __init__(self, data=None, h=None, closed=None, **kwargs):
       super().__init__("deriv3", {"data" : data, "h" : h, "closed" : closed, **kwargs})

class complex(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("complex", {"list" : list, **kwargs})

class c_mul(OpenSCADObject):
    def __init__(self, z1=None, z2=None, **kwargs):
       super().__init__("c_mul", {"z1" : z1, "z2" : z2, **kwargs})

class _split_complex(OpenSCADObject):
    def __init__(self, data=None, **kwargs):
       super().__init__("_split_complex", {"data" : data, **kwargs})

class _combine_complex(OpenSCADObject):
    def __init__(self, data=None, **kwargs):
       super().__init__("_combine_complex", {"data" : data, **kwargs})

class _c_mul(OpenSCADObject):
    def __init__(self, z1=None, z2=None, **kwargs):
       super().__init__("_c_mul", {"z1" : z1, "z2" : z2, **kwargs})

class c_div(OpenSCADObject):
    def __init__(self, z1=None, z2=None, **kwargs):
       super().__init__("c_div", {"z1" : z1, "z2" : z2, **kwargs})

class c_conj(OpenSCADObject):
    def __init__(self, z=None, **kwargs):
       super().__init__("c_conj", {"z" : z, **kwargs})

class c_real(OpenSCADObject):
    def __init__(self, z=None, **kwargs):
       super().__init__("c_real", {"z" : z, **kwargs})

class c_imag(OpenSCADObject):
    def __init__(self, z=None, **kwargs):
       super().__init__("c_imag", {"z" : z, **kwargs})

class c_ident(OpenSCADObject):
    def __init__(self, n=None, **kwargs):
       super().__init__("c_ident", {"n" : n, **kwargs})

class c_norm(OpenSCADObject):
    def __init__(self, z=None, **kwargs):
       super().__init__("c_norm", {"z" : z, **kwargs})

class quadratic_roots(OpenSCADObject):
    def __init__(self, a=None, b=None, c=None, real=None, **kwargs):
       super().__init__("quadratic_roots", {"a" : a, "b" : b, "c" : c, "real" : real, **kwargs})

class polynomial(OpenSCADObject):
    def __init__(self, p=None, z=None, k=None, total=None, **kwargs):
       super().__init__("polynomial", {"p" : p, "z" : z, "k" : k, "total" : total, **kwargs})

class poly_mult(OpenSCADObject):
    def __init__(self, p=None, q=None, **kwargs):
       super().__init__("poly_mult", {"p" : p, "q" : q, **kwargs})

class poly_div(OpenSCADObject):
    def __init__(self, n=None, d=None, **kwargs):
       super().__init__("poly_div", {"n" : n, "d" : d, **kwargs})

class _poly_div(OpenSCADObject):
    def __init__(self, n=None, d=None, q=None, **kwargs):
       super().__init__("_poly_div", {"n" : n, "d" : d, "q" : q, **kwargs})

class _poly_trim(OpenSCADObject):
    def __init__(self, p=None, eps=None, **kwargs):
       super().__init__("_poly_trim", {"p" : p, "eps" : eps, **kwargs})

class poly_add(OpenSCADObject):
    def __init__(self, p=None, q=None, **kwargs):
       super().__init__("poly_add", {"p" : p, "q" : q, **kwargs})

class poly_roots(OpenSCADObject):
    def __init__(self, p=None, tol=None, error_bound=None, **kwargs):
       super().__init__("poly_roots", {"p" : p, "tol" : tol, "error_bound" : error_bound, **kwargs})

class _poly_roots(OpenSCADObject):
    def __init__(self, p=None, pderiv=None, s=None, z=None, tol=None, i=None, **kwargs):
       super().__init__("_poly_roots", {"p" : p, "pderiv" : pderiv, "s" : s, "z" : z, "tol" : tol, "i" : i, **kwargs})

class real_roots(OpenSCADObject):
    def __init__(self, p=None, eps=None, tol=None, **kwargs):
       super().__init__("real_roots", {"p" : p, "eps" : eps, "tol" : tol, **kwargs})

class root_find(OpenSCADObject):
    def __init__(self, f=None, x0=None, x1=None, tol=None, **kwargs):
       super().__init__("root_find", {"f" : f, "x0" : x0, "x1" : x1, "tol" : tol, **kwargs})

class _rfcheck(OpenSCADObject):
    def __init__(self, x=None, y=None, range=None, tol=None, **kwargs):
       super().__init__("_rfcheck", {"x" : x, "y" : y, "range" : range, "tol" : tol, **kwargs})

class _rootfind(OpenSCADObject):
    def __init__(self, f=None, xpts=None, ypts=None, yrange=None, tol=None, i=None, **kwargs):
       super().__init__("_rootfind", {"f" : f, "xpts" : xpts, "ypts" : ypts, "yrange" : yrange, "tol" : tol, "i" : i, **kwargs})

