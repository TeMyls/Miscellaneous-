import math
#same as matrixmath lua, but doesn't constantly create lists
#just returns points altered
#slightly less intuitive than matrix multiplication uses 2d lists


def translate_2D(tx, ty , x, y):

    #all transfornations outside the origin must be relocated to it vis this matrix first
	#and then back
    _x = x + tx
    _y = y + ty
    return _x, _y



def rotate_2D(radians, x, y):
    c = math.cos(radians)
    s = math.sin(radians)
    _x = (x * c) - (y * s)
    _y = (x * s) + (y * c)
    return _x, _y



def shear_2D(sx, sy, x, y):
    _x = x + (y * sx)
    _y = (x * sy) + y
    return _x, _y



def scale_2D(sx, sy, x, y):
    _x = x * sx
    _y = y * sy
    return _x, _y



def reflect_2D(rx, ry, x, y):
    _x = x * rx
    _y = y * ry
    return x, y 


def scale_3D(sx, sy, sz, x, y, z):
    _x = x * sx
    _y = y * sy
    _z = z * sz
    return _x, _y, _z


def reflect_3D(rx, ry, rz, x, y, z):
    _x = x * rx
    _y = y * ry
    _z = z * rz
    return _x, _y, _z


def translate_3D(tx, ty, tz, x, y, z):
    _x = x + tx
    _y = y + ty
    _z = z + tz
    return _x, _y, _z



def shear_3D(sxy, sxz, syz, syx, szx, szy, x, y, z):
    _x = x + (y * sxy) + (z * sxz)
    _y = (x * syx) + y + (z * syz)
    _z = (x * szx) + (y * szy) + z
    return _x, _y, _z



def x_rotate3D(radians, x, y, z):
    c = math.cos(radians)
    s = math.sin(radians)
    _x = x
    _y = (y * c) - (z * s)
    _z = (y * s) + (z * c)
    return _x, _y, _z



def y_rotate3D(radians, x, y, z):
    c = math.cos(radians)
    s = math.sin(radians)
    _x = (x * c) +  (z * s) 
    _y = y
    _z = (-1 * x * s) + (z * c)
    return _x, _y, _z



def z_rotate3D(radians, x, y, z):
    c = math.cos(radians)
    s = math.sin(radians)
    _x = (x * c) - (y * s) 
    _y = (x * s) + (y * c)
    _z = z
    return _x, _y, _z

