import math
import time
#import console
import os


#ASCII_brightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
#ASCII_brightness = "WM*zcvu-_+^'"
#ASCII_brightness = "WMzc+:'"

ASCII_brightness = "█▓▒░"
#print(ASCII_brightness)

floor_color = 1
wall_color = 0
player_color = 3
tile_color = 2

colors = {
	
	# wall
	wall_color:'#',
	# floor and ceiling
	floor_color:'.',
	#player
	player_color:'@',
	
	tile_color:'~'
	
}

def empty_map(rows,columns,color):
	return [[color]*columns for i in range(rows)]

def degrees_to_radians(deg):
		return (deg * math.pi)/180		
			
def angle_to(x1, y1, x2, y2):
    #in radians
    return math.atan2(y2 - y1, x2 - x1)

def distance_to(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    s = dx * dx + dy * dy
    return math.sqrt(s)

def in_bounds(x, y, w, h):
    return -1 < x < w and -1 < y < h

def clamp(x, a, b):
  return min(max(x, a), b)

class Player:
	
	def __init__(self):
		self.x = 0
		self.y = 0
		self.true_x = 0
		self.true_y = 0
		self.fov = 60
		self.angle = 90
		
		
		self.angle_inc = 45
		
		self.ground = floor_color
		self.playing = True
		self.move_angle = None
		self.possible_dir = None
		#direction decider
		self.directions = {
			#w is forward
			#a is left
			#d is right
			#s is back
			# relative to facing angle
			#angle is bounded to a multiple of 45 
			#and used to select
			#each pair is y, x
			#they are the increments at the angles
			
			#45, 90, 135, 180, 225, 270, 315, 360/0
			"w":[
				
				[1, 1],
				[1, 0],
				[1, -1],
				[0, -1],
				[-1, -1],
				[-1, 0],
				[-1, 1],
				[0, 1]
				],
				
			"a":[
				
				[-1, 1],
				[0, 1],
				[1,1],
				[1, 0],
				[1, -1],
				[0, -1],
				[-1, -1],
				[-1, 0]
				],
		
			"s":[
				
				[-1, -1],
				[-1, 0],
				[-1, 1],
				[0, 1],
				[1, 1],
				[1, 0],
				[1, -1],
				[0, -1]
				],
			
			"d": [
				
				[1, -1], 
				[0, -1], 
				[-1, -1], 
				[-1, 0], 
				[-1, 1], 
				[0, 1],
				[1, 1], 
				[1, 0]
				],	
		}
		
	def set_coords(self, x: int, y: int) -> None:
		self.x = x
		self.y = y
		self.true_x = self.x + 0.5
		self.true_y = self.y + 0.5
		
	def process_input(self, letter: str) -> None:
		self.move_angle = abs(self.angle - 45)//45
		'''
		if self.angle%45 > 0:
			self.move_angle = (self.angle - self.angle%45)/45
		else:
			self.move_angle = self.angle%45 
		
		self.move_angle = self.angle//45
		if self.angle % 45 == 0:
			self.move_angle = 0
		else:
			self.move_angle = self.angle//45
		'''
			
			
		if self.directions.get(letter):
			if self.angle == 0:
				self.move_angle = 7
			xny = self.directions[letter][self.move_angle]
			
			self.possible_dir = xny
			x_inc = xny[1]
			y_inc = xny[0]
			
			self.set_coords(self.x + x_inc,self.y + y_inc)
		else:
			
			if letter == 'e':
				self.angle = self.angle + self.angle_inc
			elif  letter == 'q':
				self.angle = self.angle - self.angle_inc
			
			
		if self.angle > 360:
				self.angle  -= 360
		elif self.angle < 0:
				self.angle += 360 
				


class MapRenderer:
	
	def __init__(self, display_grid: list[list[int]], map_grid: list[list[int]], player: Player):
		self.player = player
		self.display_grid = display_grid
		self.map_grid = map_grid
		self.cols = len(display_grid[0])
		self.rows = len(display_grid)
		self.angles = self.ray_angles(
			self.cols,
			self.player.fov)
		
	def symbol_display(self, arr2d: list[int]) -> None:
		#displays map in readable format
		h=''
		for row in arr2d:
			for col in row:
				h += colors[col] 
			h = h + '\n'
		print(h)	
		
	def ray_angles(self, ray_count: int, fov: int) -> list[float]:
		space_per_ray = degrees_to_radians(fov/ray_count)
		ray_angle = -degrees_to_radians(fov/2)
		fov_angles = []
		fov_angles.append(ray_angle)
		for i in range(ray_count):
			ray_angle = ray_angle + space_per_ray
			fov_angles.append(ray_angle)
			
		return fov_angles	
		
	def dual_map_display(self, display_grid: list[list[int]], map_grid: list[list[int]], list_hits: list[int], show_display, show_map) -> str:
		display_string = ""
		if len(display_grid) > len(map_grid):
			
			
			for row in range(len(display_grid)):
				
	
				if show_display:	
					for col in range(len(display_grid[row])):
						if colors.get(display_grid[row][col]):
							display_string += colors[display_grid[row][col]]
						else:
							display_string += str(display_grid[row][col])
							
							
				if show_map:
					if row < len(map_grid):
						for col in range(len(map_grid[row])):
							if [row , col] in list_hits:
								display_string += "o"
							elif colors.get(map_grid[row][col]):
								display_string += colors[map_grid[row][col]]
							else:
								display_string += str(map_grid[row][col])
					else:
						for col in range(len(map_grid[0])):
							display_string += '?'
						
					
							
				display_string += "\n" 
		
		elif len(display_grid) <= len(map_grid):

			
			for row in range(len(map_grid)):
				
				
				if show_display:	
					if row < len(display_grid):
						for col in range(len(display_grid[row])):
							if colors.get(display_grid[row][col]):
								display_string += colors[display_grid[row][col]]
							else:
								display_string += str(display_grid[row][col])
					else:
						for col in range(len(display_grid[0])):
							display_string += '?'
						
					
								
								
				if show_map:
					for col in range(len(map_grid[row])):
						if [row , col] in list_hits:
							display_string += "o"
						elif colors.get(map_grid[row][col]):
							display_string += colors[map_grid[row][col]]
						else:
							display_string += str(map_grid[row][col])
				
					
							
				display_string += "\n" 
				
		return display_string
		
	def render_floors(self, 
				   		x: int, 
						display_grid: list[list[int]], 
						map_grid: list[list[int]], 
						wall_height: int,
						angle_ray: list[float],
						cos: float, 
						sin: float, 
						player: Player) -> None:
		display_height = len(display_grid)
		display_width = len(display_grid[0])
		half_display_height = display_height//2
		begin = int(half_display_height + wall_height)
		for y in range(begin,display_height):
			dist = display_height/(2*y-display_height)
			#fisheye correction
			dist = dist/math.cos(angle_ray)
			
			tileX = dist * cos
			tileY = dist * sin
			tileX = math.floor(tileX + player.true_x)
			tileY = math.floor(tileY + player.true_y)
			#print(f'mx:{tileX},my:{tileY}')
			if map_grid[tileY][tileX] == tile_color:
				mfy = math.floor(y)
				mfx = math.floor(x)
				#print(f'dx:{mfx},dy:{mfy}')
				if in_bounds(mfx,mfy,len(map_grid[0]),len(map_grid)):
					display_grid[mfy][mfx] = "x"
					
			else:
				continue
	
	def DDA(self, x0: int, y0: int, x1: int, y1: int) -> list[list[int]]:
		#Digital Differential Analyser
		dx = x1 - x0
		dy = y1 - y0
		
		steps = max(abs(dx), abs(dy))
		
		x_inc = dx/steps
		y_inc = dy/steps
		
		x_start = x0
		y_start = y0
			
		coordinates = []
		for i in steps:
			x_start = x_start + x_inc
			y_start = y_start + y_inc
			
			coords = [math.floor(y_start), math.floor(x_start)]
			if coords not in coordinates:
				coordinates.append(coords)
				
		return coordinates
			
	def DDA_raycast(self, map_grid: list[list[int]], x0: float, y0: float, step_x: float,step_y: float) -> list[int]: 
	    # calculate the increment in x and y 
		xinc = step_x
		yinc = step_y
	
		# start with 1st point 
		x = x0
		y = y0
		# make a list for coordinates 
		coorinates = [] 
		coorinates.append([x, y]) 
		
		og_tile = map_grid[math.floor(y)][math.floor(x)]
		cur_tile = og_tile
		valid_tiles = [floor_color, tile_color]
		total_dist = 0
		while cur_tile == og_tile or cur_tile in valid_tiles:
			
			x = x + xinc 
			y = y + yinc 
			if in_bounds(x,y,len(map_grid[0]),len(map_grid)):
				cur_tile = map_grid[math.floor(y)][math.floor(x)]
			else:
				total_dist = distance_to(x0, y0, x, y)
				return [round(total_dist), math.floor(y), math.floor(x)]
			
			if cur_tile == wall_color:
				total_dist = distance_to(x0, y0, x, y)
				return [round(total_dist), math.floor(y), math.floor(x)]
			
				
			
		
		
			# append the x,y coordinates in respective list 
			#coorinates.append([x, y]) 
			# increment the values 
			
	def draw_vertical_line(self, display_grid: list[list[int]], x: int, color: int, size: int) -> None:
		y = 0
		if in_bounds(x, y, len(display_grid[0]), len(display_grid)):
			#start y
			y = round((len(display_grid) - size)/2)
			end_y = len(display_grid) - y
			while y < end_y:
				display_grid[y][x] = color
				y = y + 1	
							
	def render_lines(self, player: Player, map_grid: list[list[int]], display_grid: list[list[int]], angles: list[float]) -> list:
		#DDA
		distances = []
		hit_coords = []
		
		max_dim = max(len(map_grid),len(map_grid[0]))
		for ang in angles:
			#DDA by a fixed value
			#by dividing it's increments by a precision value'
			#the resulting line or raycast drawn will be more accurate to the true distance it covers
			precision = 300
			
			raycos = math.cos(ang + degrees_to_radians(player.angle))/precision
			raysin = math.sin(ang + degrees_to_radians(player.angle))/precision
			
			data = self.DDA_raycast(map_grid, player.true_x, player.true_y, raycos, raysin)
			
			dist = data[0]
			hit_coord_x = data[1]
			hit_coord_y = data[2]
			#fisheye correction
			dist *= math.cos(raycos)
			distances.append(dist)
			hit_coords.append([hit_coord_x, hit_coord_y])
		
		#print(player.true_x, player.true_y)
		#print(hit_coords)
		#print(distances)
		#print(max_dim)
			
			
		for i in range(len(distances)):
			percent = ((max_dim - distances[i])/(max_dim  + distances[i]))
			#print(percent)
			#line_len = round(self.rows * percent)
			line_len = round(self.rows * ((max_dim - distances[i])/max_dim))/1.2
			#line_len = distances[i]%len(map_grid)
			#line_len = round(self.rows * ((max_dim - distances[i])/max_dim))
			
			bright_index = round((1 - percent) * (len(ASCII_brightness) - 1))
			#print(bright_index, len(ASCII_brightness))
			choice_color = ASCII_brightness[bright_index]
			
			raycos = math.cos(angles[i] + degrees_to_radians(player.angle))
			
			raysin = math.sin(angles[i] + degrees_to_radians(player.angle))
			
			#wall drawing
			self.draw_vertical_line(display_grid, i, choice_color, line_len)
			#floor drawing
			#
			#self.render_floors(i,display_grid,map_grid,line_len,angles[i],raycos,raysin,player)
			
			
		
	
		return [distances, hit_coords]
		
	def animate(self, wait = False) -> None:
		if wait:
			time.sleep(.5)
		# for Windows
		os.system('cls')

		# for Pythonista
		#console.clear()
		self.display_grid.clear()
		
	def update(self) -> None:
		
		self.display_grid = empty_map(self.rows,self.cols,floor_color)
		
		data = self.render_lines(self.player,self.map_grid,self.display_grid, self.angles)
																						
		dist_list = data[0]
		hit_list = data[1]
		
		show_map = True
		show_display = True
		is_animated = True
		
		display_string = self.dual_map_display(self.display_grid,self.map_grid,hit_list,show_display,show_map)
					
		#self.player.process_input(letters)
		print(display_string)
		#print(f'loc:{self.player.x} {self.player.y}')
		#print('Angle: {}'.format(self.player.angle))
		print('Move Angle: {}'.format(self.player.move_angle))
		#if self.player.move_angle:
		#	print(f"PDir:{self.player.possible_dir}")
		dir = input(f"Move?")
			
		#dir processing
		for letter in dir:
			
			if is_animated and len(dir) > 1:
				self.display_grid = empty_map(self.rows,self.cols,floor_color)
				data = self.render_lines(self.player,self.map_grid,self.display_grid, self.angles)
													
													
													
				dist_list = data[0]
				hit_list = data[1]
				
				display_string = self.dual_map_display(self.display_grid,self.map_grid,hit_list,show_display,show_map)
				#symbol_display(map_display)
				print(display_string)
				print("Animated Move Queue")
				self.animate(True)
				#time.sleep(.5)
				#console.clear()
				#os.system('cls')
			
			prev_x = self.player.x
			prev_y = self.player.y
			self.player.process_input(letter)
			
			
			if self.map_grid[self.player.y][self.player.x] == wall_color:
				#if the player is in a wall
				self.player.set_coords(prev_x,prev_y)
			else:
				#setting the groud tile to whatever is beneath
				self.map_grid[prev_y][prev_x] = self.player.ground
				#setting the groud tile to whatever is beneath
				self.player.ground = self.map_grid[self.player.y][self.player.x]
				#setting the ground to the player color
				self.map_grid[self.player.y][self.player.x] = player_color
			
			if letter == "x":
				self.player.playing = False
				print("Quitted")
			
			
		
		self.animate()
			
			
			
class GameLoop:
	def __init__(self, display_map, true_map):
		self.player = Player()
		self.player.set_coords(1,2)
		self.map_handler = MapRenderer(display_map, true_map,self.player)
		
	def run(self) -> None:
		self.map_handler.map_grid[self.player.y][self.player.x] = player_color
		while self.player.playing:
			self.map_handler.update()



_true_map = [
	
	[0,0,0,0,0],
	[0,1,1,1,0],
	[0,1,1,1,0],
	[0,1,1,1,0],
	[0,0,0,0,0]
	
]

_true_map = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,0,0,0,1,0,0,1,1,1,1,0,0,0],
	[0,1,0,0,0,1,0,0,1,1,1,1,0,0,0],
	[0,1,1,1,1,1,0,0,1,0,0,1,0,1,0],
	[0,1,1,1,1,0,0,0,1,1,0,1,1,1,0],
	[0,1,1,1,1,0,0,0,1,0,0,1,1,1,0],
	[0,0,0,1,1,0,0,0,1,0,0,1,0,1,0],
	[0,0,0,1,1,1,1,1,0,1,1,1,1,1,0],
	[0,0,0,1,1,1,1,0,1,1,1,0,0,1,0],
	[0,0,0,1,1,1,1,0,1,1,1,0,0,1,0],
	[0,0,0,1,1,1,1,1,1,1,1,0,0,1,0],
	[0,0,0,1,0,0,0,0,1,0,1,0,0,1,0],
	[0,0,0,1,0,0,0,1,1,1,1,0,0,1,0],
	[0,0,0,1,0,0,0,1,1,1,1,1,1,1,0],
	[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	
	]
	
true_map = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,2,1,1,0,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,0,1,1,1,1,0],
	[0,1,1,1,0,0,0,0,1,0,1,1,2,1,0],
	[0,1,1,1,0,1,1,0,1,0,1,1,1,1,0],
	[0,1,1,1,0,1,1,0,1,0,1,1,1,1,0],
	[0,1,1,1,0,1,1,0,1,0,1,1,1,1,0],
	[0,1,1,1,0,1,1,0,1,0,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,0,1,1,1,1,1,0],
	[0,1,1,1,1,2,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,2,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	]



rows = 20
cols = 45
display_map = empty_map(rows,cols,floor_color)
				
GameLoop(display_map, true_map).run()