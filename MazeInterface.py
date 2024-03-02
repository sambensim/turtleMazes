#MazeInterface
import MazeGen,AStarInGrid
from turtle import done
def main():
    print('Enter Desired Maze Width: ')
    columns = int(input()) #I know this isn't safe but fix later
    print('\nEnter Desired Maze Height: ')
    rows = int(input())
    print('\ngenerating maze...')
    connections = MazeGen.generateMaze(rows,columns)
    print('drawing maze...')
    MazeGen.drawMaze(connections,rows,columns)
    print('maze drawn')
    print('\nEnter \'s\' to view solution, \'ds\' to view solution and animated search, \'a\' to solve with A*,\'da\' to view A* solution and animated search, \'p\' to view generation path: ')
    answer = input()
    if answer=='s' or answer=='ds':
        print('\nsolving maze...')
        if answer=='s':
            draw = False
        else:
            draw = True
        path=AStarInGrid.RecursiveSearch(AStarInGrid.connectionDict(connections),0,0,rows*columns-1,columns,draw=draw)
        print('maze solved')
        print('drawing solution...')
        AStarInGrid.drawSolution(path,columns)
        print('solution drawn')
    elif answer=='p':
        print('drawing paths...')
        MazeGen.drawPaths(connections,columns)
        print('paths drawn')
    elif answer=='a' or answer=='da':
        if answer=='a':
            draw = False
        else:
            draw = True
        print('\nsolving maze...')
        path=AStarInGrid.AStar(AStarInGrid.connectionDict(connections),0,rows*columns-1,columns,draw=draw)
        print('maze solved')
        print('drawing solution...')
        AStarInGrid.drawSolution(path,columns)
        print('solution drawn')
    done()



if __name__ == '__main__':
    main()
