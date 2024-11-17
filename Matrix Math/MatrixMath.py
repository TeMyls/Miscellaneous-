import random
import console
import math
import numpy as np

def display(arr2d):
	for i in arr2d:
		print(i)
		
def set_matrix2D(x, y):
	matrix_2D = [
		[x],
		[y],
		[1]
		]
	return matrix_2D
	
def set_matrix3D(x, y, z):
	matrix_3D = [
		[x],
		[y],
		[z],
		[1]
		]
	return matrix_3D

def get_2D_vertices(matrix2D):
	#after multiplication
	x = matrix2D[0][0]
	y = matrix2D[1][0]
	return x, y
	
def get_3D_vertices(matrix3D):
	#after multiplication
	x = matrix3D[0][0]
	y = matrix3D[1][0]
	z = matrix3D[2][0]
	return x, y, z

def blank_matrix2D():
	"""
	is origin centric
	[[x],
	[y],
	[1]]
	a matrix that would do nothing when multipled
	puts transforations in context
	"""
	blank_matrix = [
		[1, 0, 0],
		[0, 1, 0],
		[0, 0, 1]
		]
	return blank_matrix

def translation_matrix2D(tx , ty):
	"""
	all transfornations outside the origin must be relocated to it vis this matrix first
	and then back
	[[x],
	[y],
	[1]]
	"""
	translation_matrix = [
		[1, 0, tx],
		[0, 1, ty],
		[0, 0, 1]
		]
	return translation_matrix
		
		
def rotation_matrix2D(radians):
	
	c = math.cos(radians)
	s = math.sin(radians)
	rotation_matrix = [
		[c, s, 0],
		[-s, c, 0],
		[0, 0, 1]
		]
	return rotation_matrix
	
def shear_matrix2D(sx, sy):
	
	shear_matrix = [
		[1, sx, 0],
		[sy, 1, 0],
		[0, 0, 1]
		]
	return shear_matrix
	
def scale_matrix2D(sx, sy):
	
	scale_matrix = [
		[sx, 0, 0],
		[0, sy, 0],
		[0, 0, 1]
		]
	return scale_matrix
	
def reflect_matrix2D(rx, ry):
	"""
	sx = -1 and sy = -1 reflects about the origin
	sx = 1 and sy = -1 reflects about x axis
	sx = -1 and sy = 1 reflects about y axis
	"""
	reflect_matrix = [
		[rx, 0, 0],
		[0, ry, 0],
		[0, 0, 1]
		]
	return reflect_matrix
	
def blank_matrix3D():
	blank_matrix = [
		[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[1, 0, 0, 1]
		]
	return blank_matrix
	
def reflection_matrix3D(rx,ry,rz):
	#use 1 or -1
	reflect_matrix = [
		[rx, 0, 0, 0],
		[0, ry, 0, 0],
		[0, 0, rz, 0],
		[1, 0, 0, 1]
		]
	return reflect_matrix
	
def scale_matrix3D(sx, sy, sz):
	scale_matrix = [
		[sx, 0, 0, 0],
		[0, sy, 0, 0],
		[0, 0, sz, 0],
		[1, 0, 0, 1]
		]
	return scale_matrix
	
def translation_matrix3D(tx, ty, tz):
	translation_matrix = [
		[1, 0, 0, tx],
		[0, 1, 0, ty],
		[0, 0, 1, tz],
		[1, 0, 0, 1]
		]
	return translation_matrix
	
def shear_matrix3D(sxy,sxz,syz,syx,szx,szy):
	shear_matrix = [
		[1, sxy, sxz, 0],
		[syx, 1, syz, 0],
		[szx, szy, 1, 0],
		[1, 0, 0, 1]
		]
	return shear_matrix
	
	
def x_rotation_matrix3D(radians):
	c = math.cos(radians)
	s = math.sin(radians)
	rotation_matrix = [
		[1, 0, 0, 0],
		[0, c, -s, 0],
		[0, s, c, 0],
		[1, 0, 0, 1]
		]
	return rotation_matrix
	
def y_rotation_matrix3D(radians):
	c = math.cos(radians)
	s = math.sin(radians)
	rotation_matrix = [
		[c, 0, s, 0],
		[0, 1, 0, 0],
		[-s, 0, c, 0],
		[0, 0, 0, 1]
		]
	return rotation_matrix

def z_rotation_matrix3D(radians):
	c = math.cos(radians)
	s = math.sin(radians)
	rotation_matrix = [
		
		
		[c, -s, 0, 0],
		[s, c, 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1]
		]
	return rotation_matrix
	
def matrix_addition(a_matrix, b_matrix):
	rows_a = len(a_matrix)
	cols_a = len(a_matrix[0])
	rows_b = len(b_matrix)
	cols_b = len(b_matrix[0])
	if rows_a != rows_b or cols_a != cols_b:
		print("both matrices must be the same dimesions")
		return
	elif rows_a == 0 or rows_b == 0 or cols_a == 0 or cols_a == 0:
		print("Empty")
	
	result = new_matrix(rows_a,cols_a)
	print(a_matrix)
	print(b_matrix)
	for y in range(rows_a):
		product = 0
		for x in range(cols_a):
			product = a_matrix[y][x] + b_matrix[y][x]
			result[y][x] = product
			
	for i in result:
		print(i)
	return result
	
def scalar_matrix_multiply(scalar, matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	
	
	result = new_matrix(rows,cols)
	
	for y in range(rows):
		product = 0
		for x in range(cols):
			product = matrix[y][x] * scalar
			
	for i in result:
		print(i)
	return result
	
def scalar_matrix_divide(scalar, matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	
	
	result = new_matrix(rows,cols)
	
	for y in range(rows):
		product = 0
		for x in range(cols):
			product = matrix[y][x] / scalar
			
	for i in result:
		print(i)
	return result
			
			
def matrix_subtraction(a_matrix, b_matrix):
	
	
	rows_a = len(a_matrix)
	cols_a = len(a_matrix[0])
	rows_b = len(b_matrix)
	cols_b = len(b_matrix[0])
	
	
	if rows_a != rows_b or cols_a != cols_b:
		print("both matrices must be the same dimesions")
		return
	elif rows_a == 0 or rows_b == 0 or cols_a == 0 or cols_a == 0:
		print("Empty")
	
	result = new_matrix(rows_a,cols_a)
	print(a_matrix)
	print(b_matrix)
	for y in range(rows_a):
		product = 0
		for x in range(cols_a):
			product = a_matrix[y][x] + b_matrix[y][x]
			result[y][x] = product
			
	for i in result:
		print(i)
	return result
	

	
def matrix_transpose(matrix):
	rows = len(matrix)
	cols = len(matrix[0])

	transposed = []
	for i in range(cols):
		new_row = []
		for j in range(rows):
			new_row.append(matrix[j][i])
			transposed.append(new_row)

	return transposed
	
def new_matrix(rows,cols):
	return [[0]*cols for i in range(rows)]

def matrix_multiply(a_matrix, b_matrix):
	rows_a = len(a_matrix)
	cols_a = len(a_matrix[0])
	rows_b = len(b_matrix)
	cols_b = len(b_matrix[0])
	
	if cols_a != rows_b and rows_a != cols_b:
		print("Matrix \"A\"s columns must be equal to Matrix \"B\"s rows")
		return 
	elif rows_a == 0 or rows_b == 0 or cols_a == 0 or cols_a == 0:
		print("Empty Matrix")
		return 
		
	print(f"A rows: {rows_a} A cols: {cols_a}")
	display(a_matrix)
	print(f"B rows: {rows_b} B cols: {cols_b}")
	display(b_matrix)
	
	result = []
	if rows_a == cols_b or cols_a == rows_b:
		a = []
		b = []
		if rows_a == cols_b and cols_a == rows_b:
			if rows_a + cols_b < cols_a + rows_b:
				a = b_matrix
				b = a_matrix
			else:
				a = a_matrix
				b = b_matrix 
		elif rows_a == cols_b:
			a = a_matrix
			b = b_matrix

		elif cols_a == rows_b:
			a = b_matrix
			b = a_matrix
			
		for by in range(len(b)):
			new_row = []
			for ax in range(len(a[0])):
				product = 0
				for bx in range(len(b[0])):
					#print(a[bx][ax]," times ", b[by][bx])
					product += a[bx][ax] * b[by][bx]
				new_row.append(product)
			result.append(new_row)
					
				
			
	
		
	print()
	display(result)
	return result		
	
			
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

		
matrix_a = [
	[2, 1, 1, 1, 5]
	]
	
matrix_b = [
	[1],
	[0],
	[2]
	]

ortho_projection = [
		[1, 0, 0],
		[0, 1, 0]
		
		
	]

	
matrix_ap = [
	[2, 5, 1],
	[6, 7, 1],
	]

matrix_xyz = [
		[0],
		[2],
		[6]
	]
	
matrix_xy = [
		[2],
		[2]
	]
	

matrix_multiply(A, B)
matrix_multiply(B, A)
print('numpy dot')
print(np.dot(np.array(A), np.array(B)))


#matrix_multiply(matrix_a, matrix_b)
#print(np.dot(np.array(matrix_b), #np.array(matrix_a)))
v = set_matrix2D(2, 3)
display(v)
print(get_2D_vertices(v))
#print(None)
#matrix_multiply(matrix_b, matrix_a)

