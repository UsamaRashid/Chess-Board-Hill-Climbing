# Chess Board Hill Climbing

This code implements a hill climbing algorithm to solve the N-Queens problem on a chessboard. The goal is to place N queens on an N×N chessboard such that no two queens threaten each other.

## Code Overview

The code is written in Python and consists of the following main parts:

1. **ChessBoard**: It defines an 8x8 chessboard represented as a 2D list. Each element in the list represents a cell on the chessboard, and a value of 1 represents the presence of a queen in that cell.

2. **printBoard**: This function is used to print the current state of the chessboard.

3. **placeQueen**: This function randomly places queens on the chessboard by setting the value of corresponding cells to 1.

4. **CheckRight**: This function checks for queens attacking in the same row to the right of the given cell.

5. **CheckUpDiagonal**: This function checks for queens attacking in the diagonal above and to the left of the given cell.

6. **CheckDownDiagonal**: This function checks for queens attacking in the diagonal below and to the left of the given cell.

7. **objectiveFunc**: This function calculates the number of queens attacking each other on the chessboard.

8. **hillClimbing**: This function implements the hill climbing algorithm to find a solution to the N-Queens problem. It iteratively searches for a better state by moving queens to positions that reduce the number of attacks. The algorithm terminates when it reaches a state where no better moves can be made.

9. **Main Function**: The main function initializes the chessboard, places queens on it, and then calls the objective function to calculate the number of attacks. Finally, it calls the hillClimbing function to find an optimal solution to the problem.

## Usage

To use this code, simply run it in a Python environment. The chessboard and the initial placement of queens can be modified by uncommenting one of the predefined chessboard configurations. The output will display the initial chessboard, the number of queens attacking each other, and the final chessboard after applying the hill climbing algorithm.

Note: The code currently assumes an 8x8 chessboard, but it can be easily modified to work with different board sizes by adjusting the size of the `ChessBoard` list and the arguments passed to the functions.

Feel free to experiment with different configurations and board sizes to solve the N-Queens problem!