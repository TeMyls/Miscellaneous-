
from MatrixMath import *
#from numpy import eye, dot, linalg, array, uint8
#from numpy import array, uint8, linalg, radians
import numpy as np
import math


floor_color = 1

wall_color = 0
player_color = 7
other_color = 9

colors = {
	#wall
	wall_color:'.',
	#floor
	floor_color:'#',
	#player
	player_color:'@',
    other_color:'X'
    
	
	
}

def empty_map(rows,columns,color):
	return [[color]*columns for i in range(rows)]

def symbol_display(arr):
	#displays map in readable format
	h=''
	for row in arr:
		for col in row:
			h += colors[col] + " "
		h = h + '\n'
	print(h)

def in_bounds(x, y,grid_w,grid_h):
    return 0 <= x < grid_w and 0 <= y < grid_h 



class Vertex():
    def __init__(self, x , y):
        self.v = np.array(
            set_matrix2D(x, y)
        )

    def get_X(self):
        return self.v[0, 0]

    def get_Y(self):
        return self.v[1, 0]

    def __str__(self):
        return "X {} Y {}".format(self.get_X(), self.get_Y())
    
    def set_coords(self, x, y):
        self.v[0] = x
        self.v[1] = y
        self.v[2] = 1

    def transform(self, translation_matrix, transform_matrix, matrix_translation):
        
        '''
        XnY = np.linalg.multi_dot(
                            [
                            self.v,
                            translation_matrix, #moves to origin
                            transform_matrix, #applies transform
                            matrix_translation, #moves back to original position
                            
                            ] 
        )
        
        '''
        XnY = np.dot(translation_matrix, self.v) #moves to origin
        #print(XnY, '\n')
        XnY = np.dot(transform_matrix, XnY) #applies transform
        #print(XnY, '\n')
        XnY = np.dot(matrix_translation, XnY) #moves back to original position
        
        #print('nump')
        #print(XnY)
        self.set_coords(XnY[0, 0], XnY[1, 0])

grid = empty_map(30, 30, wall_color)

v = Vertex(10,5)
print(v)
ox = v.get_X()
oy = v.get_Y()
grid[oy][ox] = floor_color

cx, cy = math.floor(len(grid[0])/2), math.floor(len(grid)/2)
grid[cy][cx] = other_color
symbol_display(grid)
print(cx, cy)
#v.set_coords(2, 10)
tm = np.array(
    translation_matrix2D(-cx, -cy)
)
tfm = np.array(
    rotation_matrix2D(np.radians(180))
)
mt = np.array(
    translation_matrix2D(cx, cy)
)
v.transform(tm, tfm, mt)
nx = v.get_X()
ny = v.get_Y() 
if in_bounds(nx, ny, len(grid[0]), len(grid)):
    grid[ny][nx] = player_color
print()

print(v)
symbol_display(grid)


