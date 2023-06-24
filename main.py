import random

ChessBoard = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]


# ChessBoard =[[0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [1,1,1,1,1,1,1,1],
#             # [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0]]
# #
# ChessBoard =[[1, 0, 0, 0, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 0, 0, 1, 0, 0, 0],
#             [0, 0, 0, 0, 0, 1, 0, 0],
#             [0, 0, 0, 0, 0, 0, 1, 0],
#             [0, 0, 0, 0, 0, 0, 0, 1]]

# ChessBoard =[[0, 0, 0, 0, 0, 0, 0, 1],
#             [0, 0, 0, 0, 0, 0, 1, 0],
#             [0, 0, 0, 0, 0, 1, 0, 0],
#             [0, 0, 0, 0, 1, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0, 0, 0]]

def printBoard(name):
    for objs in name:
        print(objs)


def placeQueen(chessBoard):
    x = len(chessBoard)
    y = len(chessBoard[0])

    # print("X: ",x,"Y: ",y)
    for a in range(x):
        randomva = random.randint(0, y - 1)
        for b in range(y):
            if (randomva == b):
                # print(b,"  ",a)
                chessBoard[b][a] = 1


def CheckRight(chessBoard, row, col):
    x = len(chessBoard)
    y = len(chessBoard[0])
    queens = 0
    for a in range(0, y):
        if (a < x and a != col):
            if (chessBoard[row][a] == 1):
                # print("Right :",row,a)
                queens += 1
    return queens


def CheckUpDiagonal(chessBoard, row, col):
    x = len(chessBoard)
    y = len(chessBoard[0])
    queens = 0
    ncols = col
    nrows = row
    while ((ncols >= 0) and (nrows < x)):
        ncols -= 1
        nrows += 1
    # print("UPDIAGONAl: ",ncols,nrows)
    ncols += 1
    nrows -= 1

    indexExist = 0
    tempncols = ncols
    tempnrows = nrows
    while ((tempncols < y) and (tempnrows >= 0)):
        if (chessBoard[tempncols][tempnrows] == 1 and tempncols != col and tempnrows != row):
            indexExist = 1
            # print("founddddddddddddddddddddddddddddddddddddddddddddddddd :",tempncols,tempnrows)
        tempncols += 1
        tempnrows -= 1

    if (indexExist == 1):
        while (ncols < y):
            if ((ncols >= 0) and (ncols != row) and (nrows != col) and (nrows < y)):
                if (ChessBoard[ncols][nrows] == 1):
                    queens += 1
                    # print("attackkkkkkkkkkkkkkkkkkkkkkkkkkkUP:",ncols,nrows)
                # print("U_Dia: X:", ncols, "Y:", nrows)
            ncols += 1
            nrows -= 1

        return queens
    else:
        return 0


def CheckDownDiagonal(chessBoard, row, col):
    x = len(chessBoard)
    y = len(chessBoard[0])
    queens = 0
    ncols = col
    nrows = row
    while ((ncols != 0) & (nrows != 0)):
        ncols -= 1
        nrows -= 1
    # print("DOWN DIAGONAL: ", ncols, nrows)

    indexExist = 0
    tempncols = ncols
    tempnrows = nrows
    while ((tempncols < x) and (tempnrows < x)):
        if (chessBoard[tempncols][tempnrows] == 1 and tempncols != col and tempnrows != row):
            indexExist = 1
            # print("founddddddddddddddddddddddddddddddddddddddddddddddddd :",tempncols,tempnrows)
        tempncols += 1
        tempnrows += 1

    if (indexExist == 1):
        while (nrows < y):
            if ((nrows >= 0) and (nrows != col) and (ncols != row) and (ncols < y)):
                if (ChessBoard[ncols][nrows] == 1):
                    queens += 1
                    # print("attackkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkDOWN:", ncols, nrows)
                # print("U_DOWN: X:", ncols, "Y:", nrows)
            ncols += 1
            nrows += 1
        # #
        return queens
    else:
        return 0
    # return 0


def objectiveFunc(chessBoard):
    x = len(chessBoard)
    y = len(chessBoard[0])
    queens = 0

    for a in range(x):
        for b in range(y):
            if (chessBoard[a][b] == 1):
                # print(b,"  ",a)
                # print(a," ",b)
                temp = CheckRight(chessBoard, a, b)
                queens += temp
                temp = CheckUpDiagonal(chessBoard, a, b)
                queens += temp
                temp = CheckDownDiagonal(chessBoard, a, b)
                queens += temp
    return queens


# def tempBoard(chessboard,row,col,newx,newy):


def hillClimbing(chessBoard, noOfRow, noOfCol):
    x = len(chessBoard)
    y = len(chessBoard[0])

    # print(x,y)
    index = 0
    neighbours = []
    OriginalChessBoard = chessBoard
    CurrBoardObj = -1

    while (CurrBoardObj > 1):
        for a in range(x):
            for b in range(y):

                tempchessBoard1 = OriginalChessBoard
                tempchessBoard2 = OriginalChessBoard
                tempchessBoard3 = OriginalChessBoard
                tempchessBoard4 = OriginalChessBoard

                originalAttacks = objectiveFunc(OriginalChessBoard)
                print("originalAttacks", originalAttacks)
                neighbourAttack1 = -1
                neighbourAttack2 = -1
                neighbourAttack3 = -1
                neighbourAttack4 = -1
                if (chessBoard[a][b] == 1):
                    # print("A,b ")
                    print("index:", index)
                    index += 1
                    print("Hill :", a, b)
                    x1 = a - 1
                    x2 = a + 1
                    y1 = b - 1
                    y2 = b + 1
                    # -adding possible neigbours
                    # print("       Coor",x1,x2,y1,y2)
                    if (x1 >= 0):
                        # neighbours.append((x1,b))
                        tempchessBoard1[a][b] = 0
                        tempchessBoard1[x1][b] = 1
                        neighbourAttack1 = objectiveFunc(tempchessBoard1)
                        # print(chessBoard[x1][b])
                    if (x2 < x):
                        # neighbours.append((x2,b))
                        tempchessBoard2[a][b] = 0
                        tempchessBoard2[x2][b] = 1
                        neighbourAttack2 = objectiveFunc(tempchessBoard2)

                    if (y1 >= 0):
                        # neighbours.append((a,y1))
                        tempchessBoard3[a][b] = 0
                        tempchessBoard3[a][y1] = 1
                        neighbourAttack3 = objectiveFunc(tempchessBoard3)
                    if (y2 < y):
                        # neighbours.append((a,y2))
                        tempchessBoard4[a][b] = 0
                        tempchessBoard4[a][y2] = 1
                        neighbourAttack4 = objectiveFunc(tempchessBoard4)
                    print("OBJS:", neighbourAttack1, neighbourAttack2, neighbourAttack3, neighbourAttack4)
                    # CHANGING ITS position to point where min obj function
                    if (
                            neighbourAttack1 < neighbourAttack2 and neighbourAttack1 < neighbourAttack3 and neighbourAttack1 < neighbourAttack4 and neighbourAttack1 < originalAttacks and neighbourAttack1!=-1 ):
                        # OriginalChessBoard[a][b] = 0
                        # OriginalChessBoard[x1][b] = 1
                        # CurrBoardObj=objectiveFunc(OriginalChessBoard)
                        OriginalChessBoard = tempchessBoard1
                        CurrBoardObj = neighbourAttack1
                    elif (
                            neighbourAttack2 < neighbourAttack1 and neighbourAttack2 < neighbourAttack3 and neighbourAttack2 < neighbourAttack4 and neighbourAttack2 < originalAttacks and neighbourAttack1!=-1):
                        # OriginalChessBoard[a][b] = 0
                        # OriginalChessBoard[x2][b]=1
                        # CurrBoardObj=objectiveFunc(OriginalChessBoard)
                        OriginalChessBoard = tempchessBoard2
                        CurrBoardObj = neighbourAttack2
                    elif (
                            neighbourAttack3 < neighbourAttack1 and neighbourAttack3 < neighbourAttack2 and neighbourAttack3 < neighbourAttack4 and neighbourAttack3 < originalAttacks and neighbourAttack1!=-1):
                        # OriginalChessBoard[a][b] = 0
                        # OriginalChessBoard[a][y1]=1
                        # CurrBoardObj=objectiveFunc(OriginalChessBoard)
                        OriginalChessBoard = tempchessBoard3
                        CurrBoardObj = neighbourAttack3

                    elif (
                            neighbourAttack4 < neighbourAttack1 and neighbourAttack4 < neighbourAttack2 and neighbourAttack4 < neighbourAttack3 and neighbourAttack4 < originalAttacks and neighbourAttack1!=-1):
                        # OriginalChessBoard[a][b] = 0
                        # OriginalChessBoard[a][y2] = 1
                        # CurrBoardObj=objectiveFunc(OriginalChessBoard)
                        OriginalChessBoard = tempchessBoard4
                        CurrBoardObj = neighbourAttack4

                    print("No of Queens attack Now :", CurrBoardObj)
    print("So the Final Board with O attacks would be: ")
    for objs in OriginalChessBoard:
        print(objs)

        # for every neighbour calulate objective func.....
        # for objs in neighbours:
        #
        #     print(objectiveFunc(chessBoard[objs[0]][objs[1]]))


if __name__ == '__main__':
    print("Inital Chest Board")
    printBoard(ChessBoard)
    placeQueen(ChessBoard)
    print("Chest Board After Placing queens")
    printBoard(ChessBoard)
    print("Calling the Objective Function....")
    no = objectiveFunc(ChessBoard)
    print("Number of queens attacking each other is :", no)
    hillClimbing(ChessBoard, 8, 8)
    # print(ChessBoard[0][0], "  ",ChessBoard[2][2], "  ",ChessBoard[3][3],"  ",ChessBoard[5][5],"  ",ChessBoard[7][7])

