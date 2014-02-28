def pour_problem(X,Y,goal,start=(0,0)):

	if goal in start:
		return [start]
	explored= set()
	frontier=[[start]]

	while frontier:

		path = frontier.pop(0)
		(x,y) = path[-1]
		for (state, action) in successors(x, y, X, Y).items():
			if statei not in explored:
				explored.add(state)
				path2 = path + [action,state]
				if goal in state:
					return path2
				else:
					frontier.append(path2)
	return Fail
Fail=[]	


def successors(x, y, X, Y):

	assert x <= X and y <= Y
	possible_states={}

	if (X > x):
		possible_states[(X,y)] = 'fill X'
	if (Y > y):
		possible_states[(x,Y)] = 'fill Y'
	if (x!=0):
		possible_states[(0,y)] = 'empty X'
	if (y!= 0):
		possible_states[(x,0)] = 'empty Y'

	possible_states[(x+y,0) if (x+y<=X) else (X, y-(X-x))]='Y -> X'
	possible_states[(0,x+y) if (x+y<=Y) else (x-(Y-y), Y)]='X -> Y'
	print (possible_states)
	return possible_states



print(pour_problem(4,9,6))

