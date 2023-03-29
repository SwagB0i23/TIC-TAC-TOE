from IPython.display import clear_output


print(                                   'WELCOME TO TIC TAC FUCKING TOE!!!!!')
print('\n\n\n Practice program by CJ\n\n')
# PLAYERS SHOULD BE 2
# FLOW SHOULD GO LIKE THIS
# DISPLAY THE BOARD -- PLAYER 1 MOVES -- UPDATE THE BOARD -- PLAYER 2 MOVES

def slot_input():
    slot = input('\nPlease select from slots 1-9 to place a marker: ')
    while slot not in ['1','2','3','4','5','6','7','8','9']:
        display_board(board)
        print('\nPlease select only numbers from 1-9!')
        slot = input('\nPlease select from slots 1-9 to place a marker: ')
        print('\n'*100)
    return int(slot)

def marker_input():
    display_board(board)
    marker = input('\nPlease select which marker to place (X or O): ')
    while marker not in ['X','O','x','o']:
        display_board(board)
        print('NOT AN X or an O!')
        marker = input('\nPlease select which marker to place (X or O): ')
        print('\n'*100)
    return marker.upper()

def display_board(board):

    print (f'         {board[1:4]}')
    print (f'         {board[4:7]}')
    print (f'         {board[7:10]}')

def marker_replacer(slot,marker):
    board[slot] = str(marker)

def check(board):
    checkx = ['X', 'X', 'X']
    checko = ['O', 'O', 'O']
    if counter == 10:
        return False
    else:
        pass


    for i in range(len(board)):
        #HORIZONTALS
        if board[1:4] == checkx or board[1:4] == checko:
            return False
        elif board[4:7] == checkx or board[4:7] == checko:
            return False
        elif board[7:10] == checkx or board[7:10] == checko:
            return False
        #VERTICALS
        elif board[1:8:3] == checkx or board[1:8:3] == checko:
            return False
        elif board[3:10:3] == checkx or board[3:10:3] == checko:
            return False
        elif board[2:9:3] == checkx or board[2:9:3] == checko:
            return False
        #DIAGONALS
        elif board[1:10:4] == checkx or board[1:10:4] == checko:
            return False
        elif board[3:8:2] == checkx or board[3:8:2] == checko:
            return False
        else:
            return True

def prevclose():
    prevclose_input = input('\n\nPress any key to close.')
    return prevclose_input

def counter():
    x = 1
    while game_on:
        x += 1
        return True
    if x == 9:
        return False
#TEST RUN!

#GAME ON!
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
game_on = True

counter = 1

while game_on:

#DISPLAY EMPTY BOARD:
    display_board(board)

#SLOT AND MARKER INPUT:
    slot = slot_input()
    print('\n'*100)
    marker = marker_input()

#RUN REPLACER:
    marker_replacer(slot,marker)
    display_board(board)

    print('\n'*100)


#CHECKER:

    counter += 1
    game_on = check(board)
    print('\n'*100)


#CONGRATS:

else:
    print('GAME OVER!')

prevclose()
