'''
 Display the game instruction
 determine who goes first
 create an emoty tic-tac-toe board
 display the board
 while nobody's won andit's not a tie
    if its's the human's turn
    get the human's move
    update the board with the move
otherwise
    calculate the computer's move
    update the board with the move
disply the board
swiitch turns
congratulate the winner or declare a tie

'''


# Tic Tac Toe
# Plays the game of tic-tac-toe against a human opponent

# global constants


X = "X"  # value for x
O = "O"  # value for o
EMPTY = " "
TIE = "TIE" # global variable that shows if the match ends in a tie
NUM_SQUARES = 9  # number of squares on the box


def display_instruct():
    """
        Display game instructions.
    """
    print(
        """
        Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
        This will be a showdown between your human brain and my silicon processor.
        You will make your move known by entering a number, 0 - 8. The number will correspond to the board position as illustrated:

                                0 | 1 | 2
                                ---------
                                3 | 4 | 5
                                ---------
                                6 | 7 | 8

        """
    )


def ask_yes_no(question):
    """
        This function basically ask a yes or no question
    """
    response = None  # player response
    while response not in ("y", "n"):
        response  = input(question).lower() # converts what the user inputs to a lower string
    return response



def ask_number(question, low, high):
    """
        This function ask the user to input a number withi the range
    """
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """
        This Function Determines if player or computer goes first
    """
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == 'y':
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
        # print("Human becomes",human)
        # print("Computer becomes", computer)
    else:
        print("\nYour bravery will be your undoing... I will go first")
        computer = X
        human = O
        # print("Human becomes",human)
        # print("Computer becomes", computer)    
    return computer, human

def new_board():
    """
    This function creates a new game board
    """
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """
    Display the game board in screen
    """    
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8])


def legal_moves(board):
    """
    Create A List Of Legal Moves
    """
    moves = [] # legal moves
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square) # appends the empty cell to the list of legal moves
    return moves

def winner(board):
    """
        Determines the game winner
    """
    WAYS_TO_WIN = (
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE
        
    return None        


def human_move(board, human):
    """
        Get The Human Move
    """
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human. Choose another.\n")
    print("Fine...")
    return move

def computer_move(board, computer, human):
    """
        Make A Computer Move
         - If there's a move that allows the computer to win this turn, the computer should
         choose that move
         - If there's a move that allows the human to win next turn, the computer should chose 
         that move
         - Otherwise, the computer shuold choose the best empty square as it move. The
         best square is the center . The next best squares are the corners. And the next best
         squares are the rest
    """
    # make a copy to work with since function will be changing list
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7) # best moves in order
    print("I shall the square number", end=" ")


    # If computer can win, take the that move
    for move in legal_moves(board):
        board[move]  = computer
        if winner(board) == computer:
            print(move)
        board[move] = EMPTY
    
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
        board[move] = EMPTY
    

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """
    Switch turns.
    """
    if turn == X:
        return O
    else:
        return X



def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n ")


    
    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more.\n Proof that computers are superior to humans in all regards.")
    elif the_winner == human:
        print("No, no!It cannot be!But never again!Somehow you tricked me, human. \n I, the computer, so swear it!")
    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me. \nCelebrate today... for this is the best you will ever achieve.")


if __name__ == '__main__':
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)


    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        
        display_board(board)
        turn = next_turn(turn)
    
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
    input("\nPress the enter key to quit.")







# display_instruct() # call the display_instruct function




