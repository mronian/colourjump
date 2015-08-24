# colourjump
A* Search Implementation of the Popular Colour Jump game

###Input
```
Size of Board (N)
Number of Colours (C)
<Row1>
<Row2>
..
..
<RowN>
```
Example Input 

```
4
3
1 2 2 1
2 1 3 2
3 1 3 2
0 2 3 0
```
###Output
![Alt text](/Screenshots/Output.png)

###State

1 1 2 2

2 1 3 2

3 1 3 2

0 2 3 0

###Goal

The final goal state consists of all states having just one ball of one colour. 

###Heuristic

Number of colours left on the board -1

###Gameplay

1. Take board start state from input file.

2. Initialise Priority Queue with this state

3. Proceed to A* Search

4. For each state taken from priority queue, check if goal state is reached :

- If YES, proceed to print the path from start->goal state.
  
- If NO, continue with A* search.
  
5. Neighbours of a state are found by:

- Finding locations of all zeros
  
- For each zero, find the possible moves to fill it in the up, down, left and right directions
  .
-  For each such move, get the configuration of the next board state.
  
-  All the above states will be neighbours of the current state.
  
6. The Program also stores moves between 2 configurations of the board for printing the moves at the end.

7. Proceed with A* Search by finding f-values of all the board states and adding to priority queue.

