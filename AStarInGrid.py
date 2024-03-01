#A* in random maze
from sys import setrecursionlimit
import MazeGen, turtle
def main():
    rows = 120
    columns = rows
    connections = MazeGen.generateMaze(rows,columns)
    MazeGen.drawMaze(connections,columns,rows)
    connection_dict = connectionDict(connections)
    path=AStar(connection_dict,0,0,rows*columns-1,columns)
    drawSolution(path,rows,columns)

def drawSolution(path,rows,columns):
    window = turtle.Screen()
    window.tracer(60)
    t=turtle.Turtle()
    t.color('red')
    t.hideturtle()
    for value_index in range(1,len(path)):
        MazeGen.drawConnection(path[value_index-1],path[value_index],columns,1,t)
    MazeGen.drawConnection(path[-2],path[-1],columns,1,t)

def AStar(connection_dict,start,current,goal,columns,parent=-1): #assuming a grid, uses A* pathfinding to get from the current cell to the goal, returning the order cells are visited
    setrecursionlimit(1000000) 
    if current==goal:
        return [current]
    neighbors = connection_dict[current]
    costs = {}
    for neighbor in neighbors:
        if neighbor!=parent:
            costs[neighbor]=cost(start,neighbor,goal,columns)
    neighbors = sorted(costs)
    for neighbor in costs:
        if neighbor!=parent:
            path_list=AStar(connection_dict,start,neighbor,goal,columns,current)
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

if __name__ == '__main__':
    main()