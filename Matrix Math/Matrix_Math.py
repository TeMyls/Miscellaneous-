import math
#same as matrixmath lua, but doesn't constantly create lists
#just returns points altered
#slightly less intuitive than matrix multiplication uses 2d lists

def translate_2D(tx, ty , x, y):

    #all transfornations outside the origin must be relocated to it vis this matrix first
	#and then back

    x = x + tx
    y = y + ty
    return x, y


def rotate_2D(radians, x, y):
    x = (x * math.cos(radians)) - (y * math.sin(radians))
    y = (x * math.sin(radians)) + (y * math.cos(radians))
    return x, y



def shear_2D(sx, sy, x, y):
    x = x + (y * sx)
    y = (x * sy) + y
    return x, y



def scale_2D(sx, sy, x, y):
    x = x * sx
    y = y * sy
    return x, y 



def reflect_2D(rx, ry, x, y):
    x = x * rx
    y = y * ry
    return x, y 


def scale_3D(sx, sy, sz, x, y, z):
    x = x * sx
    y = y * sy
    z = z * sz
    return x, y, z


def reflect_3D(rx, ry, rz, x, y, z):
    x = x * rx
    y = y * ry
    z = z * rz
    return x, y, z


def translate_3D(tx, ty, tz, x, y, z):
    x = x + tx
    y = y + ty
    z = z + tz
    return x, y, z



def shear_3D(sxy, sxz, syz, syx, szx, szy, x, y, z):
    x = x + (y * sxy) + (z * sxz)
    y = (x * syx) + y + (z * syz)
    z = (x * szx) + (y * szy) + z
    return x, y, z



def x_rotate3D(radians, x, y, z):
    x = x
    y = (y * math.cos(radians)) - (z * math.sin(radians))
    z = (y * math.sin(radians)) + (z * math.cos(radians))
    return x, y, z



def y_rotate3D(radians, x, y, z):
    x = (x * math.cos(radians)) +  (z * math.sin(radians)) 
    y = y
    z = (-1 * x * math.sin(radians)) + (z * math.cos(radians))
    return x, y, z



def z_rotate3D(radians, x, y, z):
    x = (x * math.cos(radians)) - (y * math.sin(radians)) 
    y = (x * math.sin(radians)) + (y * math.cos(radians))
    z = z
    return x, y, z

