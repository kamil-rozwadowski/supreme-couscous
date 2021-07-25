import random
X='X'
O='O'
empty = " "
INSTRUCT='''
Hello GAMER in my new game.
It is called Tik Tac Toe.
You will play AI.
It will be hard but who knows maybe you will win.

This is numeration of the board 


| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |

GOOD LUCK !!!
'''


def help():
    print(INSTRUCT)


def board_print(board):
    print(' |',board[0],'|','| ',board[1],'|','|',board[2],'|\n ------------------ \n',
          '|',board[3],'|','| ',board[4],'|','|',board[5],'|\n ------------------ \n',
          '|',board[6],'|','| ',board[7],'|','|',board[8],'| \n \n')
def change_turn(turn):
    if turn == 1:
        turn = 0
    else:
        turn = 1
    return turn


def start():
    question=input('Do you wanna make first move ? Type yes or no : \n')
    if question.lower()=='yes':
        return 1
    elif question.lower()=='no':
        return 0
    else:
        print("Wrong answer try again")
        return start()


def move(board):
    move = int(input('Where you wanna do your move ?\n'))
    while 0 < 1:
        if board[move] == " ":
            board[move] = X
            return board
        else:
            print('This square is taken')
            move = int(input('Where you wanna do your move ?\n'))
def pc_move(board,lvl=2):
    win_move = ((0, 3, 6), (1, 4, 7), (2, 5, 8), (3, 4, 5), (0, 1, 2), (6, 7, 8), (0, 4, 8), (2, 4, 6))
    if lvl == 1:
        while 0 < 1:
            move = random.randint(0,8)
            if board[move] == " ":
                if board[move] == " ":
                    board[move] = O
                    return board
    elif lvl == 2:
        board = board[:]
        for row in win_move:
            if ((board[row[0]] == board[row[1]] == O) and (board[row[2]] == empty)):
                board[row[2]] = O
                return board
            elif( (board[row[1]] == board[row[2]]== O) and (board[row[0]] == empty)):
                board[row[0]] = O
                return board
            elif ((board[row[0]] == board[row[2]]== O) and (board[row[1]] == empty)):
                board[row[1]] = O
                return board
            elif ((board[row[0]] == board[row[1]] == X) and (board[row[2]] == empty)):
                board[row[2]] = O
                return board
            elif( (board[row[1]] == board[row[2]]== X) and (board[row[0]] == empty)):
                board[row[0]] = O
                return board
            elif ((board[row[0]] == board[row[2]]==X) and (board[row[1]] == empty)):
                board[row[1]] = O
                return board
            else:
                best_moves=[4,0,2,6,8,1,3,5,7]
                for move in best_moves:
                    if board[move] == " ":
                        if board[move] == " ":
                            board[move] = O
                            return board




def main():
    help()
    board = [empty, empty, empty, empty, empty, empty, empty, empty, empty]
    turn = start()
    end = 0
    win_move=((0,3,6),(1,4,7),(2,5,8),(3,4,5),(0,1,2),(6,7,8),(0,4,8),(2,4,6))
    lvl=int(input('Choose difficulty: 1 - easy, 2 - medium \n'))
    while end == 0:
        if turn == 1:
            board = move(board)
        else:
            board = pc_move(board,lvl)
        board_print(board)
        turn = change_turn(turn)
        for row in win_move:
            if board[row[0]] == board[row[1]] == board[row[2]] !=empty:
                if board[row[0]] == X:
                    end = 1
                    break
                else:
                    end = 2
                    break
        if empty not in board:
            end = 3
    if end == 1:
        print('NICE YOU WIN')
    elif end == 2:
        print('OHHHHHHHHH YOU ARE LOOOOOOSER')
    else:
        print('It is tie')
main()

input('press enter to exit')