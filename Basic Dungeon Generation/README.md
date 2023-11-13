# Basic Dungeon Generation
First using my implementation of the ![Binary Space Partitioning Algorithm](https://github.com/TeMyls/Miscellaneous-/tree/main/BSP%20-%20Binary%20Space%20Partitioning). I split a 2d array into multiple subsections.<br />
![](https://github.com/TeMyls/Miscellaneous-/blob/main/Basic%20Dungeon%20Generation/BSPsubdivisions2.PNG)<br />
![](https://github.com/TeMyls/Miscellaneous-/blob/main/Basic%20Dungeon%20Generation/BSPsubdivisions.PNG)
Then within those subsections, a room of a random width and height is placed and tunnels are generating connecting the rooms<br />
![](https://github.com/TeMyls/Miscellaneous-/blob/main/Basic%20Dungeon%20Generation/generatedmap2.PNG)<br />
![](https://github.com/TeMyls/Miscellaneous-/blob/main/Basic%20Dungeon%20Generation/generatedmap.PNG)

You may have noticed there are two testmap files, the main difference between the two is the method of tunnel generation.<br />
In both methods the centers of two room is used. In one method a the two centers form the edges of a rectangle, which the top and left or the bottom and right of the rectangle will become tunnels. In another method, the midpoint of the north, south, east, and west of each rooms are derived from the coordinates of the center of the room. Then a distance check is preformed between the two rooms and whichever midpoints are closest to each other are used to make to random points along the wall the midpoints aligned with. Then depending on the alignmenent of those two points, be they on the north, south, east, or west wall. They will form different types of tunnels. If the two directions are opposite of one another, say a north wall connecting to a south wall, one straight tunnel will be drawn extending from the wall's alignment, onces these tunnels are equal they are connected. If the two alignments aren't directly opposite, they do the same thing mentioned in the first method, but instead of using the two centers of the rooms as rectangle's edges. The two randomly chosing closest points are instead.


![](https://github.com/TeMyls/Miscellaneous-/blob/main/Basic%20Dungeon%20Generation/TestMapvsTestMap3.png)
