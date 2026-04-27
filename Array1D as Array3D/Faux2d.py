def get_faux2D(array, row, col, rows, cols):
	#indexing a 1D array as if it were a 2D array
	return array[(row % rows) * cols + (col % cols)]
	
def set_faux2D(array, row, col, rows, cols, value):
	#indexing a 1D array as if it were a 2D array
	array[(row % rows) * cols + (col % cols)] = value
	return array
	
def show_faux(array, rows, cols):
	s = ""
	for y in range(rows):
		
		for x in range(cols):
			s += str(get_faux2D(array, y, x, rows, cols)) + " "
		s += "\n"
	return s