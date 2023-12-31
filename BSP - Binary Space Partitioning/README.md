# Binary Space Partitioning
Binary Space Partitioning or BSP consists of dividing an 2d array or grid into many subsections.
<br /> This article was the basis of this to help me conceptually understand the algorithm.<br />
["Rogue Basin article on BSP Dungeon Generation"](https://www.roguebasin.com/index.php/Basic_BSP_Dungeon_generation)
["BSP in Unity Game Engine"](https://medium.com/@guribemontero/dungeon-generation-using-binary-space-trees-47d4a668e2d0)

Most BSP dungeon generation algorithms use the tree data struction.
<br /> The way my generation works is by using the queue data structure. <br /> It works as follows.

* The square represents the X, Y, Width, and Height of the 2d Array or Grid as in an array within a larger array represented by the brackets in the image.
* It's further split into two subsections each with their own array and the larger square removed from the queue
* This spliting continues until the larger array is equal to the amount of subsections desired. 

![](https://github.com/TeMyls/Miscellaneous-/blob/main/BSP%20-%20Binary%20Space%20Partitioning/BSPqueuevisualization.png)

# Results
The reason why the subsections are so lopsided in some cases is that the vertical or horizontal splitting is random. 
<br />This can be remedied by replacing the 'rand' variable with 1 or 0 so the similar layouts are generated each time.

![](https://github.com/TeMyls/Miscellaneous-/blob/main/BSP%20-%20Binary%20Space%20Partitioning/BSPsubdivisions.PNG)

![](https://github.com/TeMyls/Miscellaneous-/blob/main/BSP%20-%20Binary%20Space%20Partitioning/BSPsubdivisions2.PNG)
