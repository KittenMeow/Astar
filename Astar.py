import string
import random
import math





col = 5
row = 5

board = [['A' for y in range(col)] for x in range(row)] # Make the board


def printboard():
	for thing in board:
		print(thing)
	print("\n\n")




m = random.randint(0,4)
n = random.randint(0,4)
board[m][n] = 'E' # Set the End in the board
j = random.randint(0,4)
i = random.randint(0,4)
board[i][j] = 'S' # Set the Start in the board
pos = board[i][j]







printboard() # Printing the board


def is_end():
	if pos == 'E':
		print("Yayyyy")
		printboard()

def find_cue():
	global neighbor1, neighbor2, neighbor3, neighbor4
	
	try:
		neighbor1 = board[i-1][j]
		neighbor2 = board[i+1][j]
		neighbor3 = board[i][j-1]
		neighbor4 = board[i][j+1]
		neighbors = ["board[i-1][j]", "board[i+1][j]", "board[i][j-1]", ""]
	except IndexError:
		neighbor1 = board[i-1][j]
		neighbor3 = board[i][j-1]
	except IndexError:
		neighbor4 = board[i][j+1]
		neighbor2 = board[i+1][j]
	except IndexError:
		neighbor1 = board[i-1][j]
		neighbor4 = board[i][j+1]
	except:
		neighbor2 = board[i+1][j]
		neighbor3 = board[i][j-1]
		
	global cue
	
	try:
		cue = [neighbor1, neighbor2, neighbor3, neighbor4]
	except NameError:
		cue = [neighbor1, neighbor3]
	except NameError: 
		cue = [neighbor2, neighbor4]
	except NameError:
		cue = [neighbor1, neighbor4]
	except:
		cue = [neighbor2, neighbor3]
		

find_cue()
print(cue)

def find_dis():
	global distances
	distances = { random.randint(1, 9) : q for q in cue }


def find_pos():
	global cd, rd
	if i - m == 0:
		rd = 0
		print("s is in same row as e ", abs(rd))

	elif i - m < 0:
		rd = i - m 
		print("s is above e by ", abs(rd), " row(s) ", abs(rd))

	elif i - m > 0:
		rd = i - m 
		print("s is below e by ", i - m, " row(s) ", abs(rd))

	else:
		print("Error: ", i - m , " is not a thing")

	if j - n == 0:
		cd = 0
		print("s is in the same column as e ", abs(cd))
		
	elif j - n < 0:
		cd = j - n
		print("s is to the left of e by ", abs(cd), " column(s) ", abs(cd))
		
	elif j - n > 0:
		cd = j - n
		print("s is to the right of e by ", abs(cd), " column(s) ", abs(cd))
	else:
		print("Error: ", j - n, " is not a thing")
	
		
find_pos()
find_dis()


part1 = abs(cd) + abs(rd)
part2 = list(distances.keys())
w = 0
itr2 = iter(part2)
fullpart = []
while w < len(part2):
	try:
		fullpart.append(part1 + part2[w])
	except IndexError:
		break
	w = w + 1

print(fullpart)
print(part2)
print(distances)

if 'E' in distances:
	pos = 'E'
	is_end()
	
	
