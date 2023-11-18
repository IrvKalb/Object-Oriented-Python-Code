# Object-Oriented-Python
 
This repository contains code from the book, "Object-Oriented Python".

Written by:  Irv Kalb

Book published in December 2021, published by No Starch Press

Link to book:  https://nostarch.com/object-oriented-python

-----------------------------------

## New free game available:

I have finally released my first Python-based game on itch.io.  It is free to download and play (Mac and Windows):

https://irvkalb.itch.io/rats

This is a highly challenging 80's style retro shooter game.  Here is a link to the How to Play video:

https://www.youtube.com/watch?v=nX_oFR27g2g

The game was developed using heavy doses of object-oriented programming, which is the subject of my book "Object-Oriented Python".

Please check out the game - I hope you enjoy it.

-----------------------------------
## Important notice about pygame

As of Python 3.11, a new branch of pygame, named "pygame-ce" (community edition), must be used.  (The details of this are too complex to go into here.)  In all printings of Object-Oriented Python, there are these installations instructions for the pygame package:

Page 90:  Installing the pygame package.  The page says to enter these commands at the command line:

    python3 -m pip install -U pip --user  
    python3 -m pip install -U pygame --user  

To install the community edition of pygame, you must first uninstall the older version of pygame if you have already installed it. Here are the updated commands that you should use at the command line.:

    python3 -m pip install -U pip --user  
    python3 -m pip uninstall -U pygame --user  
    python3 -m pip install -U pygame-ce --user  

After installing pygame-ce, you do NOT need to change anything to use the example code from the book. In fact, the import statement:

    import pygame

will work to bring in the new pygame-ce package.

----------------------------------


I have posted a two-part video on how to make object-oriented buttons in
for use in pygame-based programs.  You can view them here:

Part 1:  https://youtu.be/Sw-x9xUCZRg
Part 2:  https://youtu.be/NgKNyaJgMSo

The information in the videos comes from the book.

---
The documentation for my "pygwidgets" package can be found here:

   https://pygwidgets.readthedocs.io
   
And the documentation of my "pyghelpers" package can be found here:

   https://pyghelpers.readthedocs.io
