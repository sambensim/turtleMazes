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
    print('\nEnter \'s\' to view solution or \'p\' to view generation path: ')
    answer = input()
    if answer=='s':
        print('\nsolving maze...')
        path=AStarInGrid.AStar(AStarInGrid.connectionDict(connections),0,0,rows*columns-1,columns)
        print('maze solved')
        print('drawing solution...')
        AStarInGrid.drawSolution(path,rows,columns)
        print('solution drawn')
    elif answer=='p':
        print('drawing paths...')
        MazeGen.drawPaths(connections,columns)
        print('paths drawn')
    done()



if __name__ == '__main__':
    main()