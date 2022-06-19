from typing import List, Union
import random


Board: List[str] = ['-' for item in range(9)]

currentPlayer: str = 'X'
winner: Union[str, None] = None
gameRunning: bool = True


def printBoard(Board: List[str]) -> None:
     print("Places for your help:")
     print("1 | 2 | 3")
     print("4 | 5 | 6")
     print("7 | 8 | 9\n")
     print("Game On:")
     print(Board[0],"|",Board[1],"|",Board[2])
     print(Board[3],"|",Board[4],"|",Board[5])
     print(Board[6],"|",Board[7],"|",Board[8])

def userInput(Board: List[str]) -> None:
        value: int = int(input("Enter your place between 1 to 9: "))

        if value >= 1 and value <= 9 and Board[value-1] == '-':
            Board[value-1] = currentPlayer
        else:
            print("Either entered value is incorrect or place is occupied. Please Try Again !!!")

def checkHorizontal(Board: List[str]) -> bool:
    global winner
    if Board[0]==Board[1]==Board[2] and Board[1] != '-':
        winner = Board[0]
        return True
    elif Board[3]==Board[4]==Board[5] and Board[4] != '-':
        winner = Board[3]
        return True
    elif Board[6]==Board[7]==Board[8] and Board[7] != '-':
        winner = Board[6]
        return True

def checkVertical(Board: List[str]) -> bool:
    global winner
    if Board[0]==Board[3]==Board[6] and Board[3] != '-':
        winner = Board[0]
        return True
    elif Board[1]==Board[4]==Board[7] and Board[4] != '-':
        winner = Board[1]
        return True
    elif Board[2]==Board[5]==Board[8] and Board[5] != '-':
        winner = Board[2]
        return True

def checkDiagonal(Board: List[str]) -> bool:
    global winner
    if Board[0]==Board[4]==Board[8] and Board[4] != '-':
        winner = Board[0]
        return True
    elif Board[2]==Board[4]==Board[6] and Board[4] != '-':
        winner = Board[2]
        return True

def checkWin(Board: List[str]) -> None:
    global gameRunning
    if checkHorizontal(Board) or checkVertical(Board) or checkDiagonal(Board):
        printBoard(Board)
        print("GAME OVER!")
        print(f"Congratulations! {winner} won the game!!!")
        gameRunning = False

def checkTie(Board: List[str]) -> None:
    global gameRunning
    if '-' not in Board:
        printBoard(Board)
        print("GAME OVER!")
        print('It is a Tie !!!')
        gameRunning = False

def switchPlayer() -> None:
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

def computer(Board: List[str]) -> None:
    global currentPlayer
    if currentPlayer == 'O':
        position = random.randint(0,8)
        Board[position] = currentPlayer
        switchPlayer()

def choosePlayer2(player: str) -> None:
    if player == '1':
        while gameRunning:
            printBoard(Board)
            userInput(Board)
            checkWin(Board)
            checkTie(Board)
            switchPlayer()
    elif player == '2':
        while gameRunning:
            printBoard(Board)
            userInput(Board)
            checkWin(Board)
            checkTie(Board)
            switchPlayer()
            computer(Board)


if __name__=="__main__":
    player2 = input("Enter (1) for player2 and (2) for computer: ")
    choosePlayer2(player2)

