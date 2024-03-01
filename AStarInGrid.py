#A* in random maze
#Note that this isn't truly A* as newly 'discovered' points are always checked first - only those are sorted by cost
from sys import setrecursionlimit
import MazeGen, turtle
def main():
    rows = 50
    columns = rows
    connections = MazeGen.generateMaze(rows,columns)
    MazeGen.drawMaze(connections,columns,rows)
    connection_dict = connectionDict(connections)
    path=RecursiveSearch(connection_dict,0,0,rows*columns-1,columns,draw=True)
    drawSolution(path,columns)
    turtle.done()

def drawSolution(path,columns):
    window = turtle.Screen()
    window.tracer(60)
    t=turtle.Turtle()
    t.color('red')
    t.hideturtle()
    for value_index in range(1,len(path)):
        MazeGen.drawConnection(path[value_index-1],path[value_index],columns,1,t)
    MazeGen.drawConnection(path[-2],path[-1],columns,1,t)

def RecursiveSearch(connection_dict,start,current,goal,columns,parent=-1,draw=False): #assuming a grid, uses recursive pathfinding to get from the current cell to the goal, returning the order cells are visited
    setrecursionlimit(1000000)
    if draw:
        t=turtle.Turtle()
        t.hideturtle()
        t.color('blue')
        window=turtle.Screen()
        window.tracer(60)
    if current==goal:
        return [current]
    neighbors = connection_dict[current]
    costs = {}
    for neighbor in neighbors:
        if neighbor!=parent:
            costs[neighbor]=cost(start,neighbor,goal,columns)
    neighbors = sorted(costs,reverse=True)
    for neighbor in neighbors:
        if draw:
            MazeGen.drawConnection(current,neighbor,columns,1,t) # 1 should probably be replaced with cellsize
        if neighbor!=parent: #I don't think this if is needed
            path_list=RecursiveSearch(connection_dict,start,neighbor,goal,columns,current,draw=draw)
            if path_list!=False:
                path_list.insert(0,current)
                return path_list
    return False
        
def connectionDict(connections): #given a list of tuples of connection between nodes, returns a dictionary with each cell as a key containing a list of its neighbors
    connection_dict = {}
    for pair in connections:
        if pair[0] in connection_dict:
            connection_dict[pair[0]].append(pair[1])
        else:
            connection_dict[pair[0]]=[pair[1]]
        if pair[1] in connection_dict:
            connection_dict[pair[1]].append(pair[0])
        else:
            connection_dict[pair[1]]=[pair[0]]
    return connection_dict

def cost(start,current,goal,columns): #calculates the cost of a cell for A*
    fromStart = ((current%columns-start%columns)**2+(current//columns-start//columns)**2)**0.5
    manhattanGoal = abs(current%columns-goal%columns)+abs(current//columns-goal//columns)
    return fromStart+manhattanGoal

def AStar(connection_dict,start,goal,columns,frontier=[],draw=False):
    current,path_found = start, False
    #how can I track the path as it is traced?
    #keep track of parent so the path can be traced backwards
    while not path_found:
        for cell in connection_dict[current]:
            if cell==goal:
                path_found = True
            frontier.append(cell,cost(start,cell,goal,columns))
        min=False
        for cell in frontier:
            if min==False or cell[1]<min[1]:
                min=cell
        current = min

if __name__ == '__main__':
    main()
