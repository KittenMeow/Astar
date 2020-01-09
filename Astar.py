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
	else:
		moving()

def find_cue():
	global neighbor1, neighbor2, neighbor3, neighbor4
	
	try:
		neighbor1 = board[i-1][j]
		neighbor2 = board[i+1][j]
		neighbor3 = board[i][j-1]
		neighbor4 = board[i][j+1]
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
	distances = {}
	cueitr = iter(cue)
	distances = {q : random.randint(1,9) for q in enumerate(cueitr)}
	# try:
		# distances = {
		# neighbor1: random.randint(1,9),
		# neighbor2: random.randint(1,9),
		# neighbor3: random.randint(1,9),
		# neighbor4: random.randint(1,9),
		# }
	# except NameError:
		# distances = {
		# neighbor1: random.randint(1,9),
		# neighbor3: random.randint(1,9),
		# }
	# except NameError: 
		# distances = {
		# neighbor2: random.randint(1,9),
		# neighbor4: random.randint(1,9),
		# }
	# except NameError:
		# distances = {
		# neighbor1: random.randint(1,9),
		# neighbor4: random.randint(1,9),
		# }
	# except:
		# distances = {
		# neighbor2: random.randint(1,9),
		# neighbor3: random.randint(1,9),
		# }


find_dis()
print(distances)

def find_pos():
	global rd, cd
	if i - m == 0:
		rd = 0
		print("s is in same row as e ", rd)
	elif i - m < 0:
		rd = i - m 
		print("s is above e by ", abs(rd), " row(s) ", abs(rd))
	elif i - m > 0:
		rd = i - m 
		print("s is below e by ", i - m, " row(s) ", rd)
	else:
		print("Error: ", i - m , " is not a thing")
	if j - n == 0:
		cd = 0
		print("s is in the same column as e ", cd)	
	elif j - n < 0:
		cd = j - n
		print("s is to the left of e by ", abs(cd), " column(s) ", abs(cd))	
	elif j - n > 0:
		cd = j - n
		print("s is to the right of e by ", cd, " column(s) ", cd)
	else:
		print("Error: ", j - n, " is not a thing")
	

find_pos()
w = -1
partdist2 = abs(rd) + abs(cd)
while w < len(distances.values()):
	w = w + 1
	global partdist1
	partdist1 = []
	partdist1.append(list(distances.values()))
print(partdist1)
w = -1
global listofans
listofans = []
while w < len(partdist1[0]):
	try:
		w = w + 1
		global ans
		ans = partdist1[0][w] + partdist2
		listofans.append(ans)
		print(ans)
	except:
		break

print(listofans)




if 'E' in distances:
	pos = 'E'
	is_end()

 


def moving():
	global m, n, i, j
	global sortedans
	sortedans = sorted(listofans)
	print(sortedans)
	if board[i][j] != 'S': 
		board[i][j] == 'P'
		
	try:
		pos = sortedans[0]
	except:
		return 0
	print(pos)
	#is_end()
	remsortlist()

def remsortlist():
	global listofans
	listofans = sorted(listofans)
	try:
		del listofans[0]
	except:
		pass
	moving()
	
	
moving()
moving()

	
