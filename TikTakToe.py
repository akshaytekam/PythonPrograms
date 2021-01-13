"""
   * author - Akshay Tekam
   * date - 12/01/2021
   * time - 06:33:25
   * package - ${PACKAGE_NAME}
   * Title - Write a Program to play a Cross Game or Tic-Tac-Toe Game.
    Player 1 is the Computer and the Player 2 is the user
"""
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for i in theBoard:
    board_keys.append(i)

# print the updated board after every move
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


#  decide turns and check the winning conditions
def game():
    turn = 'X'
    count = 0

    for i in range(10):                     # for loop run for range 10 and take inputs
        printBoard(theBoard)
        print("It's " + turn + " turn. Please select location?")

        move = input()                    # input from user

        if theBoard[move] == ' ':         # check if location is empty or not
            theBoard[move] = turn
            count += 1
        else:
            print("Its already full.")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # first row
                printBoard(theBoard)
                print(turn + " won.")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # second row
                printBoard(theBoard)
                print(turn + " won.")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # third row
                printBoard(theBoard)
                print(turn + " won.")
                break
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':  # 1st diagonal
                printBoard(theBoard)
                print(turn + " won.")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # 2nd diagonal
                printBoard(theBoard)
                print(turn + " won.")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # first col
                printBoard(theBoard)
                print(turn + " won.")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # second col
                printBoard(theBoard)
                print(turn + " won.")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # 3rd col
                printBoard(theBoard)
                print(turn + " won.")
                break

                # If neither X nor O wins and the board is full
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")               # declare it draw.

        # change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

if __name__ == "__main__":
    game()