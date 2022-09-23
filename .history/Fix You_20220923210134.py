#1391B - Fix You
#Link (https://codeforces.com/problemset/problem/1391/B)
"""
Consider a conveyor belt represented using a grid consisting of n rows and m columns. The cell in the i-th row from the top and the j-th column from the left is labelled (i,j).

Every cell, except (n,m), has a direction R (Right) or D (Down) assigned to it. If the cell (i,j) is assigned direction R, any luggage kept on that will move to the cell (i,j+1). Similarly, if the cell (i,j) is assigned direction D, any luggage kept on that will move to the cell (i+1,j). If at any moment, the luggage moves out of the grid, it is considered to be lost.

There is a counter at the cell (n,m) from where all luggage is picked. A conveyor belt is called functional if and only if any luggage reaches the counter regardless of which cell it is placed in initially. More formally, for every cell (i,j), any luggage placed in this cell should eventually end up in the cell (n,m).

This may not hold initially; you are, however, allowed to change the directions of some cells to make the conveyor belt functional. Please determine the minimum amount of cells you have to change.

Please note that it is always possible to make any conveyor belt functional by changing the directions of some set of cells.
"""
