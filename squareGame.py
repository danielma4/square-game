import random

# generateBoard : Int Int -> Arr<list>[]
# fills a 2d array with random ints from 1 to maxCol to represent squares
def generateBoard(r, maxCol):
    board = [list() for i in range(int(r))]
    for x in range(int(r)):
        intRand = random.randint(1, int(maxCol) - 1)
        board[x].append(intRand)
    return board

# printBoard : Arr<list>[] -> Void (image)
# prints out a board
def printBoard(board):
    for i in range(len(board)):
        print(board[i])
    return

# binaryBoard : Arr<list>[] -> Arr<list>[]
# converts a decimal board to a binary board
def binaryBoard(bd, numBits):
    for i in range(len(bd)):
        bd[i][0] = intToBinary(bd[i][0], numBits)
    return bd


# decimalBoard : Arr<list>[] -> Arr<list>[]
# converts a binary board to a decimal board
def decimalBoard(brd):
    for i in range(len(brd)):
        brd[i][0] = binaryToInt(brd[i][0])
    return brd

# intToBinary : Int -> Int
# returns the binary (base 2) form of a decimal (base 10)
def intToBinary(n, numBits):
     binar = bin(n).replace("0b", "")
     filledBin = binar.zfill(int(bits))
     return filledBin

# binaryToInt : Int -> Int
# returns the decimal (base 10) form of a binary number (base 2)
def binaryToInt(n):
    return int(str(n), 2)

# checkEmpty : Arr<list>[] -> Bool
# checks if the board has no more squares
def checkEmpty(b):
    for i in range(len(b)):
        if b[i][0] != 0:
            return False
    return True

# countBits : Arr<list>[] -> Void
# takes in a BINARY board and adds the odd bits to a list
def countBits(b):
    for i in range(bits):
        sm = 0
        for j in range(rows):
            sm += int(b[j][0][i])
        if sm % 2 != 0:
            oddBits.append(i)

# idealMove : Arr<list>[] -> Arr<list>[]
# flips odd bits
def idealMove(b):
    if not oddBits:
        for i in range(rows):
            binaryList = list(b[i][0])
            print(binaryList)
            if all(v == '0' for v in binaryList):
                continue
            erase = list('0' for i in range(bits))
            b[i][0] = "".join(erase)
            return b
    sigBit = oddBits[0]
    for i in range(rows):
        binaryList = list(b[i][0])
        if binaryList[sigBit] == '1':
            while oddBits:
                changeBit = oddBits.pop(0)
                if binaryList[changeBit] == "0":
                    binaryList[changeBit] = "1"
                else:
                    binaryList[changeBit] = "0"
            b[i][0] = "".join(binaryList)
            return b


print("Random board generator: Enter rows desired and max amount of bits (columns represented) allowed")
rows = int(input())
bits = int(input())
maxColumns = pow(2, int(bits))
squares = generateBoard(rows, maxColumns)


binarySquares = binaryBoard(squares, bits)
decimalSquares = decimalBoard(squares)

oddBits = list()
print ("Player 1: You\nPlayer 2: Computer")
printBoard(squares)

empty = False
# just find the odd bits and reverse them
while not empty:
    print("Select a row")
    selectedRow = int(input())
    print("How many squares do you want to remove?")
    squaresRemoved = int(input())
    print("New board:")
    squares[selectedRow][0] -= squaresRemoved
    printBoard(squares)

    empty = checkEmpty(squares)
    if (empty):
        print("You win!")
        break

    squares = binaryBoard(squares, bits)
    countBits(squares)

    print("Computer move:")
    squares = decimalBoard(idealMove(squares))
    printBoard(squares)



    empty = checkEmpty(squares)
    if (empty):
        print("Better luck next time!")


    
    


