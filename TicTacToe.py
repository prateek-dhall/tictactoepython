from typing import List, Union
import random


Board: List[str] = ['-' for item in range(9)]

currentPlayer: str = 'X'
winner: Union[str, None] = None
gameRunning: bool = True


def printBoard(Board: List[str]) -> None:
    """Displays current board state and controls.

    Args:
        Board: Current board state.
    """
    print("Places for your help:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9\n")
    print("Game On:")
    print(Board[0],"|",Board[1],"|",Board[2])
    print(Board[3],"|",Board[4],"|",Board[5])
    print(Board[6],"|",Board[7],"|",Board[8])

def userInput(Board: List[str]) -> None:
    """Recives and applies user input into the board.

    Args:
        Board: Current board state.
    """
    value: int = int(input("Enter your place between 1 to 9: "))

    if value >= 1 and value <= 9 and Board[value-1] == '-':
        Board[value-1] = currentPlayer
    else:
        print("Either entered value is incorrect or place is occupied. Please Try Again !!!")

def checkHorizontal(Board: List[str]) -> bool:
    """Checks wether any player has matched 3 in horizontal line.

    Additionally sets global winner variable to the stymbol of player 
    that has won.

    Args:
        Board: Current board state.

    Returns:
        Wether horizontal check has been been found. True if yes.
    """
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
    """Checks wether any player has matched 3 in vertical line.

    Additionally sets global winner variable to the stymbol of player 
    that has won.

    Args:
        Board: Current board state.

    Returns:
        Wether vertical check has been been found. True if yes.
    """
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
    """Checks wether any player has matched 3 in diagonal line.

    Additionally sets global winner variable to the stymbol of player 
    that has won.

    Args:
        Board: Current board state.

    Returns:
        Wether diagonal check has been been found. True if yes.
    """
    global winner
    if Board[0]==Board[4]==Board[8] and Board[4] != '-':
        winner = Board[0]
        return True
    elif Board[2]==Board[4]==Board[6] and Board[4] != '-':
        winner = Board[2]
        return True

def checkWin(Board: List[str]) -> None:
    """Checks wether any player has matched 3 in any type of line.

    Additionally stops the game if game has been won.

    Args:
        Board: Current board state.
    """
    global gameRunning
    if checkHorizontal(Board) or checkVertical(Board) or checkDiagonal(Board):
        printBoard(Board)
        print("GAME OVER!")
        print(f"Congratulations! {winner} won the game!!!")
        gameRunning = False

def checkTie(Board: List[str]) -> None:
    """Checks wether the board state is a tie.

    Additionally stops the game if a tie has occurred.

    Args:
        Board: Current board state.
    """
    global gameRunning
    if '-' not in Board:
        printBoard(Board)
        print("GAME OVER!")
        print('It is a Tie !!!')
        gameRunning = False

def switchPlayer() -> None:
    """Switches current player.
    """
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

def computer(Board: List[str]) -> None:
    """A simple AI choosing a random empty board position.

    Args:
        Board: Current board state.
    """
    global currentPlayer
    if currentPlayer == 'O':
        position = random.randint(0,8)
        Board[position] = currentPlayer
        switchPlayer()

def choosePlayer2(player: str) -> None:
    """Main gamel loop.

    After reciving what type of opponent has been choosen,
    starts the main game loop.

    Args:
        player: Recived type of opponent to run the game against.
    """
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

