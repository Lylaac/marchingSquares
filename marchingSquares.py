import random

#the corresponding tile for a set of verticies. I LOVE DICTIONARIES!!!!!!
# this looks a little wierd cuz backslashes can be funky in python. just trust the process. method in the madness.
lookupDict = {
    "0000" : "   ",
    "0010" : "\  ",
    "0001" : "  /",
    "0011" : "---",
    "0100" : "  \\",
    "0110" : "/0/",
    "0101" : " |0",
    "0111" : "/00",
    "1000" : "/  ",
    "1010" : "0| ",
    "1001" : "\\0\\",
    "1011" : "00\\",
    "1100" : "---",
    "1110" : "00/",
    "1101" : "\\00",
    "1111" : "000"
}

# returns value at coords for a certain grid
def gridCheck(node, grid):
    return grid[node[0]][node[1]]

#sets value at coords for a certain grid
def gridSet(node, value, grid):
    grid[node[0]][node[1]] = value

# ok the name is self-explanatory
def printGrid(grid):
    height = len(grid)
    width = len(grid[0])
    for i in range(0, height):
        output = ["["]
        for j in range(0, width):
            node = [i, j]
            output.append(gridCheck(node, grid))
        output.append("]")
        print(''.join(output))

# returns whether a vertex is ground (1) or air (0). as we go down the chance of a 1 increases.
def randomReturner(yVal):
    probability = random.randint(0, 10)
    if probability <= yVal:
        return "1"
    else:
        return "0"
    
# yeah somehow this is like the bulk of the code
def marcher(height, width, grid):
    global mapp
    for i in range(0, height-1):
        for j in range(0, width-1): #for every node in the vertex grid
            # we get coords of the other vertices as well
            nodeTopLeft = [i, j]
            nodeTopRight = [i, j+1]
            nodeBottomLeft = [i+1, j]
            nodeBottomRight = [i+1, j+1]
            values = [gridCheck(nodeTopLeft, grid), gridCheck(nodeTopRight, grid), gridCheck(nodeBottomLeft, grid), gridCheck(nodeBottomRight, grid)] #create a list of those values
            lookup = ''.join(str(x) for x in values) #join it into a string
            gridSet(nodeTopLeft, lookupDict[lookup], mapp) #then set the correct "tile" onto the tilemap




height = 11
width = 11
#random vertex map
grid = [[randomReturner(j) for i in range(width)] for j in range(height)]
#these dont need to be here, they're just here if i want to use a custom vertex map just in case
height = len(grid)
width = len(grid[0])
#create the actual tilemap which is 1 smaller than the vertex map. this saves from out of range errors
mapp = [["0" for i in range(height-1)] for j in range(width-1)]
#run our actual functions here.
printGrid(grid)
marcher(height, width, grid)
print()
printGrid(mapp)