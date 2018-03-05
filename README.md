# Game-of-Life
This is an implementation of Conway's Game of Life (CGoL). CGoL is a cellular automaton devised by mathematician 
John Conway. The game starts with a two-dimensional grid of cells. Each cell can be either alive or dead with 
a filled-in cell typically representing a live cell and a non-filled-in cell, a dead cell. A cell's neighbors are any one 
of the eight cells surrounding that cell. When the game moves forward a step, each cell counts its number of living 
neighbors and will do one of following:

	1. If the cell is alive and its number of living neighbors is 2 or 3, the cell will continue to live.
	2. If the cell is dead and its number of living neighbors is 3, the cell will spawn.
	3. If the cell is alive and its number of living neighbors is less than 2 or greater than 3, it will die.

The borders of the cell grid in this implementation wrap around so that cells on the top are neighbors to those on the 
bottom and similarly for cells on the left and right edges.


In standard implementations of CGoL, each cell checks the state of all eight of its neighbors every time the simulation 
moves forward a step. This gives O(8n). This implementation uses an improved method of checking each cell's number of living 
neighbors that reduces the time complexity of the step function. The GameOfLife class models an instance of a CGoL simulation. 
The class uses a one-dimensional Cell list to track all the cells in the simulation. The Cell class contains a dictionary 
with elements that map to all eight neighbors of a Cell: 'top', 'left', 'bottom', 'right', 'topleft', 'bottomleft', 
'bottomright', and 'topright'. The neighbors of a Cell are set just once in the initCells() method inside the GameOfLife 
class. The initCells() method also initializes the initial number of living neighbors of each Cell. In this way, some of 
the time complexity of the step function is removed since a Cell can quickly check livingNeighbors (the variable with its 
total number of living neighbors) instead of examining each of its neighbors to determine whether it dies or lives on 
to the next generation. Using this method, a Cell, C, will only have to access its neighbors in order to update their 
livingNeighbors variable when C dies or spawns. This method will increase space complexity but results in a best 
case time complexity of O(n) and worst case of O(8n). The best case occurs when the simulation is in a stable, unchanging 
state where no cells die or spawn; the worst case occurs when the simulation is completely full of cells and every cell 
will die on the next step, causing every cell to access all eight neighbors to update each neighbors' livingNeighbors 
variable.


Something that I have not tested but suspect is an improvement to the standard CGoL implementation is the way in 
which I calculate the the neighbors of each cell. Rather than use multiple if statements which are long and hard to read 
because they have to account for the wrapping borders, I came up with some expressions which are just hard to read and 
return the position of a neighboring cell considering wrapping if the cells are stored in a one-dimensional array. 
For example, the expression: 

	(i+rowSize)%(rowSize*columnSize) 

will return the bottom neighbor of the ith cell in a one-dimensional array. So, if you have a one-dimensional array, 
cells[numCells], that contains all of cells in the simulation:
		
	cells[(i+rowSize) % (rowSize*columnSize)]

is the bottom neighbor of cells[i].


Another cool thing is that you only need expressions to calculate the top, left, bottom, and right neighbors of a 
cell. After you have calculated the neighbors at those positions, you can just do something like 

	cells[i].topLeftNeighbor = cells[i].leftNeighbor.topNeighbor

to get the remaining neighbors in the corners. And with a little modification, each of these expressions could be used in 
a two-dimensional array to get the same effect. Using a two-dimensional array, cells[columnSize][rowSize], you could get the
bottom neighbor of the cell at cells[i][j] with:

	cells[(i + 1) % columnSize][j]

In this instance, the equation for the column is the same as the one-dimensional equation but with rowSize factored out as j. 
The remaining two-dimensional neighbor-finding expressions are a little more complex to work out.


I'm not sure if using the neighbor-finding expressions is better or worse in one-dimensional or two-dimensional arrays, 
however, they both have the benefit of being less lines to code than using if statements, perhaps at the cost of being more
cryptic. Whichever method chosen, it matters little for time complexity since the neighbor-finding code is only run once in the 
beginning for every CGoL simulation. I plan to do some testing in the future to gather what if any benefits there are to using
the neighbor-finding expressions as opposed to using if statements.
