from random import shuffle
from sys import setrecursionlimit
import turtle
#Maze Gen
def main():
    connections = generateMaze(20,20)
    drawMaze(connections,20,20)
    turtle.done()

def generateMaze(rows,columns): #Uses depth-first search recursively and returns order cells are visited
    setrecursionlimit(1000000) 
    neighbors = findNeighbors(rows,columns)
    visited = []
    depthFirst(0,neighbors,visited)
    return makeConnections(visited,neighbors)

def findNeighbors(rows,columns): #Returns orthogonal cells assuming a grid map
    neighbors = {}
    for cell in range(rows*columns):
        neighbors[cell] = []
        if cell%columns!=0:
            neighbors[cell].append(cell-1)
        if cell%columns!=columns-1:
            neighbors[cell].append(cell+1)
        if cell//columns!=0:
            neighbors[cell].append(cell-columns)
        if cell//columns!=rows-1:
            neighbors[cell].append(cell+columns)
    return neighbors

def drawMaze(connections,columns,rows,cellsize=1,window_side=800): #Uses turtle to draw each line in a grid except where cells should be connected
    window = turtle.Screen()
    sch,scw = max(columns,rows)*cellsize,max(columns,rows)*cellsize
    window.setup(window_side,window_side)
    window.tracer(0) 
    turtle.setworldcoordinates(0, 0, sch, scw)
    t=turtle.Turtle()
    t.hideturtle()
    t.speed('fastest')
    walls = []
    neighbors = findNeighbors(rows,columns)
    for key in neighbors:
        for item in neighbors[key]:
            if (item,key) not in walls:
                walls.append((key,item))
    for pair in connections:
        if pair in walls:
            walls.remove(pair)
        else:
            walls.remove((pair[1],pair[0]))
    walls = optimizePath(walls,columns)
    t.penup()
    t.setx(columns*cellsize)
    t.sety(rows*cellsize)
    t.pendown()
    t.sety(0)
    t.setx(0)
    t.sety(rows*cellsize)
    t.setx(columns*cellsize)
    for pair in walls:
        drawPerpendicular(pair[0],pair[1],columns,cellsize,t)
    window.update()
    print('maze generated')

def drawPaths(connections,columns,cellsize=1): #Draws a path along the order points were generated
    t=turtle.Turtle()
    t.hideturtle()
    window=turtle.Screen()
    window.tracer(60)
    colors = ('red','blue','green')
    color_index = 0
    for pair_index in range(len(connections)):
        t.color(colors[color_index])
        if pair_index==0 or connections[pair_index][0]==connections[pair_index-1][1]:
            drawConnection(connections[pair_index][0],connections[pair_index][1],columns,cellsize,t)
        else:
            if color_index<len(colors)-1:
                color_index+=1
            else:
                color_index = 0
    window.update()

def optimizePath(walls,columns): #speeds up drawing by reducing movement where turtle pen is up
    #could be sped up by snaking rather than returning to one side each step
    #orders right to left, top to bottom,
    #also these are probably oposite because I'm drawing perpendicular lines
    vertical = [x for x in walls if x[0]//columns==x[1]//columns]
    horizontal = [x for x in walls if x not in vertical]
    horizontal.sort(key=(lambda x: x[0]//columns - 0.01*(x[0]%columns)))
    vertical.sort(key=(lambda x: x[0]%columns - 0.01*(x[0]//columns)))
    horizontal.extend(vertical)
    return horizontal

def depthFirst(currentcell,neighbors,visited): #recursive function that performs depth-first search, edits a passed list to be the order visited
    shuffle(neighbors[currentcell])
    for cell in neighbors[currentcell]:
        if cell not in visited:
            visited.append(cell)
            depthFirst(cell,neighbors,visited)

def drawPerpendicular(a,b,columns,cellsize,t): #given two cells, draws a line perpendicular to them (a wall inbetween them)
    ax,ay=a%columns,a//columns
    bx,by=b%columns,b//columns
    if ax!=bx:
        t.penup()
        t.setx(((ax+bx)/2+0.5)*cellsize)
        t.sety((ay+1)*cellsize)
        t.pendown()
        t.sety((ay-0)*cellsize)
    else:
        t.penup()
        t.setx((ax+1)*cellsize)
        t.sety(((ay+by)/2+0.5)*cellsize)
        t.pendown()
        t.setx((ax-0)*cellsize)

def drawConnection(a,b,columns,cellsize,t): #given two cells, draws a line between their centers
    ax,ay=a%columns,a//columns
    bx,by=b%columns,b//columns
    t.penup()
    t.setx((ax+0.5)*cellsize)
    t.sety((ay+0.5)*cellsize)
    t.pendown()
    t.setx((bx+0.5)*cellsize)
    t.sety((by+0.5)*cellsize)

def makeConnections(visited,neighbors): #given each node's neighbors and the order nodes are visited, returns a list of tuples of connections between nodes
    connections=[]
    for cell_index in range(1,len(visited)):
        if visited[cell_index-1] in neighbors[visited[cell_index]]:
            connections.append((visited[cell_index-1],visited[cell_index]))
        else:
            for visited_index in range(len(visited[:cell_index])):
                if visited[visited_index] in neighbors[visited[cell_index]]:
                    connection_index = visited_index
            connections.append((visited[connection_index],visited[cell_index]))
    return connections

if __name__ == '__main__':
    main()