graph = {'S':[('A',10.4),('D',8.9)], #the graph with weights
'A':[('D',8.9),('F',3),('S',11)],  #ordered by aphabetical
'B':[('E',6.9),('C',4)],
'C':[('B',6.7),('F',3),('G',4)],
'D':[('A',10.4),('E',6.9),('S',11)],
'E':[('B',6.7),('D',8.9),('F',3)],
'F':[('A',10.4),('C',4),('E',6.9)],
'G':[('C',4)]
}

#problem 2
def breathFirst():
	currentNode = 'S'
	visited = []#visited nodes
	frontier = ['S']#suppose to be a deque
	while (currentNode != 'G') :
		if visited.count(frontier[0]) > 0:#prevent revisiting nodes
			frontier.remove(frontier[0])
		else: #prevent revisiting nodes
			neighbors = graph.get(currentNode)# find neighbors
			newFrontier = [i[0] for i in neighbors] # get first elemnt in list of tuples
			frontier = frontier + newFrontier# add old frontier nodes before newer ones
			visited.append(frontier[0])
			frontier.remove(frontier[0])
			currentNode = visited[-1]

#problem3
def depthFirst():
	currentNode = 'S'
	visited = []#visited nodes
	frontier = ['S']#supose to be a deque
	while (currentNode != 'G') :
		currentNode = frontier[0]
		if visited.count(frontier[0]) > 0:#prevent revisiting nodes
			frontier.remove(frontier[0])
		else: 
			neighbors = graph.get(currentNode)# find neighbors
			newFrontier = [i[0] for i in neighbors] # get first elemnt in list of tuples
			visited.append(frontier[0])
			frontier.remove(frontier[0])
			frontier = newFrontier + frontier# add new frontier nodes before older ones

#problem 4
def bestFirst():
	currentNode = 'S'
	closedSet = []#visited nodes
	openSet = [('S',11)]#supose to be a deque of frontier nodes
	while (currentNode != 'G'):
		neighbors = graph.get(currentNode)
		openSet = neighbors + openSet
		openSet=sorted(openSet, key=lambda x: x[1])#sort frontier by distance
		if closedSet.count(openSet[0]) > 0:
			for x in range(0,len(closedSet)-1): #prevent revisiting
				openSet.remove(closedSet[x])
		closedSet.append(openSet[0])
		currentNode = openSet[0][0]#set new current node
		openSet.remove(openSet[0])


#problem 5
def beam():
	currentNode = 'S'
	closedSet = []#visited nodes
	openSet = [('S',11)]#supose to be a deque frontier nodes
	while (currentNode != 'G'):
		neighbors = graph.get(currentNode)
		openSet = neighbors + openSet
		openSet=sorted(openSet, key=lambda x: x[1])#sort frontier by distance
		for x in range(1,len(openSet)-1):
			openSet.remove(openSet[2])#keep beam at 2
		if closedSet.count(openSet[0]) > 0:
			openSet.remove(closedSet[x])# prevent revisits
		closedSet.append(openSet[0])
		currentNode = openSet[0][0]#set new current node
		openSet.remove(openSet[0])
		print currentNode

breathFirst()
depthFirst()
bestFirst()
beam()