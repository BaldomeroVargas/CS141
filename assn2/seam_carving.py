#imported libraries
import math
import sys
from decimal import *

#read in from file and contruct a matrix of size i*j
def Read_From_File():
	#temp list that
	file = open(sys.argv[1],"r")
	#imports the list and seperates by line
	image = []
	#grabs line then creates array 
	#by plitting via comma
	#stores as point bc x = energy and y = seam
	#for memeory managment
	for line in file:
		temp = str(line)
		temp.replace(" ","")
		row = temp.split(",")
		#casts strings into floats
		row = [Point(Decimal(i),Decimal(0.0)) for i in row]
		image.append(row)
	#returns the image in a 2D array from
	return image

#(x = energy value, y = seam)
class Point :
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

    def __repr__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)

def Write_to_File(filename, s):
    output = open(filename ,'w')
    output.write(str(s))
    output.write('\n')

def Write_Seam(filename, row, col, value):
    output = open(filename ,'a')
    s = "[ " + str(row) + ", " + str(col) + ", " + str(value) + " ]"
    output.write(str(s))
    output.write("\n")

#creates grid to use
grid = Read_From_File()

#gets sizes of rows and columns
r_len = len(grid[0]) 

c_len =  len(grid) 
#nested for loop of runtime O(i*j)
#grid(i,j) = grid(i,j) + min(grid(i-1,j-1),grid(i-1,j),grid(i-1,j+1))
#use above formula to calculate the minimum seam
for i in range(0,r_len):
	for j in range(0,c_len):
		if i == 0:
			grid[i][j].y = grid[i][j].x
		else:
			if j == 0 :
				grid[i][j].y = grid[i][j].x + min(Decimal('inf'),grid[i-1][j].y,grid[i-1][j+1].y) 
			elif j == c_len - 1 :
				grid[i][j].y = grid[i][j].x + min(grid[i-1][j-1].y,grid[i-1][j].y,Decimal('inf')) 
			else:
				grid[i][j].y = grid[i][j].x + min(grid[i-1][j-1].y,grid[i-1][j].y,grid[i-1][j+1].y) 
#stores c to start at
start_c = 0
#finds min seam
m_seam = grid[r_len - 1][0].y
for n in range(0,c_len):
		if m_seam > grid[r_len - 1][n].y:
			m_seam = grid[r_len - 1][n].y
			start_c = n

#outputs min seam
fname = sys.argv[1]
fname = fname[:-4]

seam_string = "Min Seam: " + str(m_seam)
Write_to_File(fname + "_trace.txt", seam_string)

#stores colummn and row of where the smallest seam is
#start_c
#start_r
ret_val = 0
temp_c = start_c
curr_r = r_len - 1

#inputs bottom row content
Write_Seam(fname + "_trace.txt", curr_r, start_c, grid[curr_r][start_c].x)

while curr_r > 0:
	curr_r = curr_r - 1
	if start_c  == 0 :
		ret_val = min(grid[curr_r][temp_c].y,grid[curr_r][temp_c+1].y) 
		if ret_val == grid[curr_r][temp_c+1].y :
			temp_c = temp_c + 1
	elif start_c  == c_len - 1 :
		ret_val =  min(grid[curr_r][temp_c-1].y,grid[curr_r][temp_c].y) 
		if ret_val == grid[curr_r][temp_c-1].y :
			temp_c = temp_c - 1
	else:
		ret_val =  min(grid[curr_r][temp_c-1].y,grid[curr_r][temp_c].y,grid[curr_r][temp_c+1].y) 
		if ret_val == grid[curr_r][temp_c+1].y :
			temp_c = temp_c + 1
		elif ret_val == grid[curr_r][temp_c-1].y :
			temp_c = temp_c - 1
		else:	
			temp_c = temp_c
	Write_Seam(fname + "_trace.txt", curr_r, temp_c, grid[curr_r][temp_c].x)
