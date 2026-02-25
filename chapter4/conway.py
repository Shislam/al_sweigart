# Conway's Game of Lige
import random, time, copy, os
SIZE = 20

# Create a list for the cells
nextCells = []
for x in range(SIZE):
    column = []
    for y in range(SIZE):
        if random.randint(0, 1) == 0:
            column.append('#') # add a living cell.
        else:
            column.append(' ') # add a dead cell
    nextCells.append(column) #nextCells is list of column lists

while True: # Main program loop
    os.system('clear')
    currentCells = copy.deepcopy(nextCells)
    
    # print currentCells on the screen
    for x in range(SIZE):
        for y in range(SIZE):
            print(currentCells[x][y], end='') 
        print()
    
    # calculate next steps cells based on current step's cells
    for x in range(SIZE):
        for y in range(SIZE):
            #Get neighboring coordinates:
            #use % WIDTH to stay in bounds
            leftCoord = (x - 1) % SIZE
            rightCoord = (x + 1) % SIZE
            aboveCoord = (y - 1) % SIZE
            belowCoord = (y + 1) % SIZE


            # count # of neighbors
            # is there a better way of doing this?
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1
            
            # rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #stay alive
                nextCells[x][y] = '#'
            
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            
            else:
                nextCells[x][y] = ' '
        
    time.sleep(1)

        