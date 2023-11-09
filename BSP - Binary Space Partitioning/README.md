Binary Space Partitioning or BSP consists of dividing an 2d array or grid into many subsections.
This article was the basis of this to help me conceptually understand the algorithm.
https://www.roguebasin.com/index.php/Basic_BSP_Dungeon_generation

Most BSP dungeon generation algorithms use the tree data struction.
The way my generation works is by using the queue data structure. It works as follows.

![](https://github.com/TeMyls/Miscellaneous-/blob/main/BSP%20-%20Binary%20Space%20Partitioning/BSPqueuevisualization.png)

The square represents the X, Y, Width, and Height of the 2d Array or Grid as in an array within a larger array represented by the brackets in the image.
It's further split into two subsections each with their own array and the larger square removed from the queue
This spliting continues until the larger array is equal to the amount of subsections desired. 
Results

![](https://github.com/TeMyls/Miscellaneous-/blob/main/BSP%20-%20Binary%20Space%20Partitioning/BSPsubdivisions.PNG)

![](https://github.com/TeMyls/Miscellaneous-/blob/main/BSP%20-%20Binary%20Space%20Partitioning/BSPsubdivisions2.PNG)
