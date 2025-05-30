# Raycasting 
Raycasting is an old technique used to render a fake 3d environment from a map in the form of a array.
<br />This version uses ASCII characters of various pixel brightness and line length to represent distance to the player.
<br /> WASD for movement, Q and E to turn 45 degrees.
<br />![](https://github.com/TeMyls/Miscellaneous-/blob/main/ASCII%20Raycasting/array_raycast.gif)
<br />This technique uses an extremely fast algorithm know. as Digital Differential Analyser or the DDA Algorithm.
<br />It's done by projecting lines or rays from the position of the player in the map until they collide with a wall, which is represented by a number in the array. Then the distance is used to project lines or rectangles of various sizes onto the screen. This simulates 3d. 
<br /> array_raycast.py is the old version without classes, raycast_array.py is the new version with classes and other minor improvements
<br />Also if an infinite loop is encountered, click the highlighted area in the console, and press CTRL + C to Keyboard Interrupt



# Articles
<br /> I learned the most from this tutorial, as I translated alot of code from Javascript to lua and watched/read alot to understand concepts
<br />["Vinicius Biavatti's Tutorial"](https://github.com/vinibiavatti1/RayCastingTutorial)
<br /> This one is far more conceptual 
<br />["Permadi's Tutorial"](https://permadi.com/1996/05/ray-casting-tutorial-table-of-contents/)
<br /> This one helped alot aswell.
<br />["Lode Vandevenne's Tutorial"](https://lodev.org/cgtutor/raycasting.html)

# Videos
<br/> Two Coding Train Videos that helped me conceptually. 
<br />["2d Raycasting"](https://youtu.be/TOEi6T2mtHo?si=VTcHfbpvmRIezg3S)
<br />["Rendering Raycasting"](https://youtu.be/vYgIKn7iDH8?si=P6GVczQUd_TRVCtk)
<br/>Javidx9 Video's explaining the DDA algorithm
<br />["Super Fast Ray Casting in Tiled Worlds using DDA"](https://youtu.be/NbSee-XM7WA?si=MkdTqBw5MWlGF6ej)
