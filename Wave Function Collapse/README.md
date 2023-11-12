# Wave Function Collapse
A great resource for understanding the Wave Function Collapse Algorithm is this [video](https://youtu.be/2SuvO4Gi7uY?si=6FCXBzKSAgtEShIk)



The wave function collapse algoritm can best be described by the puzzle game of sudoku. <br />
![](https://github.com/TeMyls/Miscellaneous-/blob/main/Wave%20Function%20Collapse/sudoku-blankgrid.png) <br />
Each cell in every row or column can only have one of a finite arrangement of numbers ranging 1 through 9. In the 3 by 3 sections in 9 by 9 grid of a normal sudoku game, if a random cell has a 9 then the entire 3 by 3 section and any cells along the cell's row and column containing the the number cannot have any 9s,limiting the other cells options to remaining cells 1 through 8.<br />
Having 9 present limits ,or __collapses__, the randomness, or __entropy__, of the cells in the 9 by 9 section and its row and column.<br />
![](https://github.com/TeMyls/Miscellaneous-/blob/main/Wave%20Function%20Collapse/edited-sudoku-blankgrid.png)<br />
Say we have 5 cells in the shape of a plus sign with two numbers,9 and 5 each perpendicular to each other on the arms of the plus sign, with only 9 the remaining possible cells in the 3 by 3 section and along it's row and column are 1 through 8, with a 5 added the possible number in the cells directly adjecent to 5 and 9 and in the 3 by 3 section would be 1 through 4 and 6 through 8,thus having 5 an 9 collapsing the possiblities. <br />
![](https://github.com/TeMyls/Miscellaneous-/blob/main/Wave%20Function%20Collapse/sudoku-grid.png)<br />
With more and more numbers added, the amount of possiblies decreases to a point where only one or very few options are left to choose, and so the guessing game begins.<br />

# The my implementation of the algorithm explained:
In the case of the grid I'm using, I have my own rules.<br /><br />
0 is a blank white cell that can be anything<br />
1 is water represented by a blue cell that only borders sand,2, and itself,1.<br />
2 is sand represented by a yellow cell that only borders water,1 , dirt,4, and itself,2.<br />
3 is a tree represented by a green cell that only borders dirt,4 , and itself,3.<br />
4 is some dirt represented by a brown cell that only borders trees,3, sand,3, and itself,4,<br />

These cells and their possible neighbors are placed in a dictionary.<br />
>options = {1:[1,2],2:[1,2,4],3:[3,4],4:[2,3,4]}
<br />

A cell of a random number ranging 1-4 is placed in a random spot on the grid. Then a random cell from its possible neighbors in the dictionary above is chosen to border it. Using the breadth first search flood fill algorithm the grid is filled out while applying the adjcent rules. If a blank cell is between two cell labeled 4 and 2 with the possible neighbors, 2,3,4 and 1,2,4, the possible options are reduced to the neighbors that only they share which are 2 and 4, and then the blank is randomly chosen from the two options.By making any cells neighbors more likely to be chosen say 2:[1,2,4] to 2:[1,1,1,2,4] it's possible to bias the randomness of chosen neighbors towards a specific outcome.<br />

# The algorithm in the console:
![](https://github.com/TeMyls/Miscellaneous-/blob/main/Wave%20Function%20Collapse/wfc.gif)
# The almost finished result

![](https://github.com/TeMyls/Miscellaneous-/blob/main/Wave%20Function%20Collapse/almostfinished.png)
</br>I lost the original.
