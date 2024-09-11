import random
import console
import math


def new_matrix(rows,cols):
	return [[0]*cols for i in range(rows)]
	
def display(arr2d):
	for i in arr2d:
		print(i)
		
def xy_rotate2d_cw(radians):
	#clockwise rotation
	#any angle
	rotation_xy = [
		[math.cos(radians),-math.sin(radians)],
		[math.sin(radians),math.cos(radians)]
		]
	return rotation_xy
	
def xy_rotate2d_cc(radians):
	#counterclockwise rotation
	#any angle
	rotation_xy = [
		[math.cos(radians),math.sin(radians)],
		[-math.sin(radians),math.cos(radians)]
		]
	return rotation_xy
	
def x_rotate3d(radians):
	rotation_x = [
		[1.0, 0.0, 0.0],
		[0.0, math.cos(radians), -math.sin(radians)],
		[0.0, math.sin(radians), math.cos(radians)]
		
		]
	return rotation_x
	
def y_rotate3d(radians):
	rotation_x = [
		[math.cos(radians),0.0, math.sin(radians)],
		[0.0, 1.0, 0.0],
		[-math.sin(radians),0.0, math.cos(radians)]
		
		]
	return rotation_x

def z_rotate3d(radians):
	rotation_x = [
		[math.cos(radians), -math.sin(radians),0.0],
		[math.sin(radians), math.cos(radians),0.0],
		[0.0, 0.0, 1.0]
		]
	return rotation_x	
	
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
	
def scalar_multiply(scalar, matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	
	
	result = new_matrix(rows,cols)
	
	for y in range(rows_a):
		product = 0
		for x in range(cols_a):
			product = matrix[y][x] * scalar
			
	for i in result:
		print(i)
	return result
	
def scalar_divide(scalar, matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	
	
	result = new_matrix(rows,cols)
	
	for y in range(rows_a):
		product = 0
		for x in range(cols_a):
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
	
		
def matrix_multiply(a_matrix, b_matrix):
	rows_a = len(a_matrix)
	cols_a = len(a_matrix[0])
	rows_b = len(b_matrix)
	cols_b = len(b_matrix[0])
	print(f"A rows: {rows_a} A cols: {cols_a}")
	display(a_matrix)
	print(f"B rows: {rows_b} B cols: {cols_b}")
	display(b_matrix)

	if cols_a != rows_b and rows_a != cols_b:
		print("Matrix \"A\"s columns must be equal to Matrix \"B\"s rows")
		return 
	elif rows_a == 0 or rows_b == 0 or cols_a == 0 or cols_a == 0:
		print("Empty Matrix")
		return 
	
	#display(a_matrix)
	#display(b_matrix)
	
	#result = new_matrix(min(rows_b,rows_a),min(cols_a,cols_b))
	
	result = []
	if rows_a == cols_b:
		result = new_matrix(rows_b,cols_a)
		for ax in range(cols_a):
			#result.append([])
			for by in range(rows_b):
				product = 0
				for bx in range(cols_b):
					print(a_matrix[bx][ax]," times ", b_matrix[by][bx])
					product += a_matrix[bx][ax] * b_matrix[by][bx]
				#result[ax].append(product)
				result[by][ax] = product
				
			#print()
	elif cols_a == rows_b:
		result = new_matrix(rows_a,cols_b)
		for bx in range(cols_b):
		#for ax in range(cols_a):
			#result.append([])
			for ay in range(rows_a):
			#for by in range(rows_b):
				product = 0
				for ax in range(cols_a):
				#for bx in range(cols_b):
					print(b_matrix[ax][bx]," times ", a_matrix[ay][ax])
					product += b_matrix[ax][bx] * a_matrix[ay][ax]
				#result[ax].append(product)
				#result[by][ax] = product
				result[ay][bx] = product
				
			#print()
			
			
		
			
	display(result)
	return result		
		
		
def matrix_multiply_2(a_matrix, b_matrix):
	rows_a = len(a_matrix)
	cols_a = len(a_matrix[0])
	rows_b = len(b_matrix)
	cols_b = len(b_matrix[0])
	print(f"A rows: {rows_a} A cols: {cols_a}")
	display(a_matrix)
	print(f"B rows: {rows_b} B cols: {cols_b}")
	display(b_matrix)

	if cols_a != rows_b and rows_a != cols_b:
		print("Matrix \"A\"s columns must be equal to Matrix \"B\"s rows")
		return 
	elif rows_a == 0 or rows_b == 0 or cols_a == 0 or cols_a == 0:
		print("Empty Matrix")
		return 
	
	#display(a_matrix)
	#display(b_matrix)
	
	#result = new_matrix(min(rows_b,rows_a),min(cols_a,cols_b))
	
	result = []
	if rows_a == cols_b or cols_a == rows_b:
		result = []
		a = []
		b = []
		if rows_a == cols_b:
			a = a_matrix
			b = b_matrix
			result = new_matrix(rows_b,cols_a)
		elif cols_a == rows_b:
			a = b_matrix
			b = a_matrix
			result = new_matrix(rows_a,cols_b)
			
		for ax in range(len(a[0])):
			#result.append([])
			for by in range(len(b)):
				product = 0
				for bx in range(len(b[0])):
					print(a[bx][ax]," times ", b[by][bx])
					product += a[bx][ax] * b[by][bx]
				#result[ax].append(product)
				result[by][ax] = product
				
			#print()
	
		
			
	display(result)
	return result						
		
		
matrix_a = [
	[2, 1, 1, 1, 1]
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

matrix_multiply_2(matrix_xyz,ortho_projection)
print()
matrix_multiply_2(ortho_projection, matrix_xyz)
#matrix_multiply(z_rotate3d(math.pi/4),matrix_xyz)
#matrix_addition(matrix_a,matrix_ap)
	
	
	
