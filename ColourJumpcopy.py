import Queue
import ast
import copy
def isGoal(board):
	counter=0
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j]!="0":
				counter+=1;
	if counter==1:
		return True
	else :
		return False

def getZeros(board):
	zeros=[]
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j]=="0":
				zeros.append((i,j))
	return zeros

def playMove(oldboard, fr, fc, tr, tc):
	board=copy.deepcopy(oldboard)
	board[tr][tc]=board[fr][fc]
	board[fr][fc]="0"
	if (fc==tc) & (fr<tr):
		for i in range(fr, tr):
			board[i][fc]="0"
	
	if (fc==tc) & (fr>tr):
		for i in range(fr, tr, -1):
			board[i][fc]="0"	

	if (fr==tr) & (fc<tc):
		for i in range(fc, tc):
			board[fr][i]="0"

	if (fr==tr) & (fc>tc):
		for i in range(fc, tc, -1):
			board[fr][i]="0"
	return board

def getBoards(zeros, board):
	boards=[]
	moves={}
	for z in zeros:
		row=z[0]
		col=z[1]
		for i in range(1,len(board)):
			if (row-i<0)|(row-i-1<0):
				break
			elif (board[row-i][col]=="0")|(board[row-i-1][col]=="0"):
				break
			elif board[row-i-1][col]!=board[row-i][col]:
				temp=playMove(board,row-i-1, col,row, col)
				boards.append(temp)
				moves[str(temp)]={str(board) : (row-i-1, col, row, col)} 
				break

		for i in range(1,len(board)):
			if (row+i>len(board)-1)|(row+i+1>len(board)-1):
				break
			elif (board[row+i][col]=="0")|(board[row+i+1][col]=="0"):
				break
			elif board[row+i+1][col]!=board[row+i][col]:
				temp=playMove(board,row+i+1, col,row, col)
				boards.append(temp)
				moves[str(temp)]={str(board) : (row+i+1, col, row, col)} 
				break

		for i in range(1,len(board)):
			if (col-i<0)|(col-i-1<0):
				break
			elif (board[row][col-i]=="0")|(board[row][col-i-1]=="0"):
				break
			elif board[row][col-i-1]!=board[row][col-i]:
				temp=playMove(board,row,col-i-1,row, col)
				boards.append(temp)
				moves[str(temp)]={str(board) : (row, col-i-1, row, col)} 
				break

		for i in range(1,len(board)):
			if (col+i>len(board)-1)|(col+i+1>len(board)-1):
				break
			elif (board[row][col+i]=="0")|(board[row][col+i+1]=="0"):
				break
			elif board[row][col+i+1]!=board[row][col+i]:
				temp=playMove(board,row,col+i+1,row, col)
				boards.append(temp)
				moves[str(temp)]={str(board) : (row, col+i+1, row, col)} 
				break
	return boards, moves

def heuristic(board):
	colours=[]
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] not in colours:
				colours.append(board[i][j])			
	return len(colours)-1

def getPath(path, goal):
	finpath=[]
	finpath.append(goal)
	while goal in path:
		goal=path[goal]
		finpath.append(goal)
	return finpath

def ColoumnJump(filename):
	fst=open(filename, 'r')
	N=fst.readline()
	num_colours=fst.readline()
	board=[]
	zeros=[]
	g={}
	neighbours=[]
	path={}
	closed=[]
	solution=[]
	moves={}
	count=0

	for line in fst.readlines():
		temp=line[0:len(line)-1].split(" ")
		board.append(temp)

	q=Queue.PriorityQueue()
	q.put(board,num_colours)
	g[str(board)]=0
	path[str(board)]=None

	while q.empty()==False:
		current=q.get()
		if isGoal(current):
			solution=getPath(path, str(current))
			break

		closed.append(current)
		zeros=getZeros(current)
		neighbours, movestemp=getBoards(zeros, current)
		
		for m in movestemp:
			if m in moves:
				moves[str(m)].update(movestemp[str(m)])
			else :
				moves[str(m)]=movestemp[str(m)]

		for n in neighbours:
			if n in closed:
				continue
			new_g=g[str(current)]+1
			if (str(n) not in g.values()):
				g[str(n)]=new_g
				priority=g[str(n)]+heuristic(n)
				q.put(n, priority)
				path[str(n)]=str(current)
			elif new_g<g[str(n)]:
				g[str(n)]=new_g
				priority=g[str(n)]+heuristic(n)
				q.put(n, priority)
				path[str(n)]=str(current)

	if solution==[]:
		print "Not Possible"
	else :
		print "\nWe found a way to win the Game!"
		print "\nGoal State Reached :"
		goal=ast.literal_eval(solution[0])
		for g in goal:
			print g
		print "\nMoves Required :"
		solution=solution[0:len(solution)-1]
		for i in range(len(solution)-1, 0, -1):
			print str(moves[solution[i-1]][solution[i]][0:2])+"->"+str(moves[solution[i-1]][solution[i]][2:4])


if __name__ == "__main__":
    import sys
    ColoumnJump(sys.argv[1])