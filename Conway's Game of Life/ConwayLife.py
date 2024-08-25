from typing import *
import math
#import console
import time
import os


class LifeGame:
	def __init__(self,board:List[List[int]],generations: int):
		self.symbol_display(board)
		self.gamefLife(generations,board)
		
	
	
	def symbol_display(self,arr):
		time.sleep(.15)
		os.system('cls')
		#console.clear()
		h=''
		for i in arr:
			for j in i:
				
				if j == 0:
					h = h + '⬜️'
				if j == 1:
					h = h +  '🟩'
				
				
			h = h + '\n'
		print(h)
	
	
	def display_board(self,board: List[List[int]]):
		for i in board:
			print(i)
			
	def update_board(self, board: List[List[int]]):
		self.symbol_display(board)
		w = len(board[0])
		h = len(board)
	
		
		cell_adj = {}
		
		
		
		for rows in range(len(board)):
			for cols in range(len(board[rows])):
				#arranged in x,y
				north = [cols + 0,rows + -1]
				north_east = [cols + 1,rows + -1]
				east = [cols + 1,rows + 0]
				south_east = [cols + 1,rows + 1]
				south = [cols + 0,rows + 1]
				south_west = [cols + -1,rows + 1]
				west = [cols + -1,rows + 0]
				north_west = [cols + -1,rows + -1]
				
				cell_name = str(cols)+'-'+str(rows)
				cell_adj.update({cell_name:0})
				
				if north[0] < w and north[0] >= 0 and north[1] < h and north[1] >= 0:
					if board[north[1]][north[0]] == 1:
						cell_adj[cell_name] += 1
						
				if north_east[0] < w and north_east[0] >= 0 and north_east[1] < h and north_east[1] >= 0:
					if board[north_east[1]][north_east[0]] == 1:
						cell_adj[cell_name] += 1
				if north_west[0] < w and north_west[0] >= 0 and north_west[1] < h and north_west[1] >= 0:
					if board[north_west[1]][north_west[0]] == 1:
						cell_adj[cell_name] += 1
				if south[0] < w and south[0] >= 0 and south[1] < h and south[1] >= 0:
					if board[south[1]][south[0]] == 1:
						cell_adj[cell_name] += 1
				if south_east[0] < w and south_east[0] >= 0 and south_east[1] < h and south_east[1] >= 0:
					if board[south_east[1]][south_east[0]] == 1:
						cell_adj[cell_name] += 1
				if south_west[0] < w and south_west[0] >= 0 and south_west[1] < h and south_west[1] >= 0:
					if board[south_west[1]][south_west[0]] == 1:
						cell_adj[cell_name] += 1
				if west[0] < w and west[0] >= 0 and west[1] < h and west[1] >= 0:
					if board[west[1]][west[0]] == 1:
						cell_adj[cell_name] += 1
				if east[0] < w and east[0] >= 0 and east[1] < h and east[1] >= 0:
					if board[east[1]][east[0]] == 1:
						cell_adj[cell_name] += 1
						
						
		for i in cell_adj:
				locs = i.split("-")
				x_coord = int(locs[0])
				y_coord = int(locs[1])
				#Cell as 1 alive
				#Cell as 0 dead
				
				#live cell with less than two neighbors die.
				if board[y_coord][x_coord] == 1:
					if cell_adj[i] < 2:
						board[y_coord][x_coord] = 0
				#any live cell with more than 3 neighbors dies as if by overpopulation
				if board[y_coord][x_coord] == 1:
					if cell_adj[i] > 3:
						board[y_coord][x_coord] = 0
						
				#Any dead cell with exactly 3 neighbors with lives as if by reproduction
				if board[y_coord][x_coord] == 0:
					if cell_adj[i] == 3:
						board[y_coord][x_coord] = 1
				#Any live cell with two or three live neighbors lives on
		
				
		
	def gamefLife(self,generations: int, board: List[List[int]]) -> None:
	#Do not return anything, modify board in-place instead.
	
		while generations > 0:
			self.update_board(board)
			self.symbol_display(board)
			generations -= 1
		print('done')
	
	
	
board = [
				[0,1,0], 
				[0,0,1],
				[1,1,1], 
				[0,0,0]
				]
				
board2 = [
	[1,1],
	[1,0]
	]

board3 = [
				[0,1,0,0,0], 
				[0,1,0,0,0], 
				[0,1,0,1,0], 
				[0,0,1,1,1], 
				[0,0,0,0,0], 
				]
				
board3 = [
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],  
				[0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],  
				[0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
				]
LifeGame(board3,300)