import sys, copy, logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)

STARTING_PIECES = {
    "a8": "bR",
    "b8": "bN",
    "c8": "bB",
    "d8": "bQ",
    "e8": "bK",
    "f8": "bB",
    "g8": "bN",
    "h8": "bR",
    "a7": "bP",
    "b7": "bP",
    "c7": "bP",
    "d7": "bP",
    "e7": "bP",
    "f7": "bP",
    "g7": "bP",
    "h7": "bP",
    "a1": "wR",
    "b1": "wN",
    "c1": "wB",
    "d1": "wQ",
    "e1": "wK",
    "f1": "wB",
    "g1": "wN",
    "h1": "wR",
    "a2": "wP",
    "b2": "wP",
    "c2": "wP",
    "d2": "wP",
    "e2": "wP",
    "f2": "wP",
    "g2": "wP",
    "h2": "wP",
}


# Checking if the board has exactly 1 white king and 1 black king.
def checkKings(board):

    # Counting the number of kings.
    white_king = 0
    black_king = 0

    # Looping through dictionary keys and adding kings if found.
    for i in board.keys():
        if board[i] == "wK":
            white_king += 1
        elif board[i] == "bK":
            black_king += 1

    # Validating the number of found kings.
    if white_king == 1 and black_king == 1:
        return True
    else:
        logging.debug("You have toom many kings.")
        return False


# Checking if each player has 16 pieces.
def checkPiecesNumber(board):

    # Counting pieces.
    white_pieces = 0
    black_pieces = 0

    # Looping through pieces and adding them up for each player.
    for i in board.keys():
        if board[i][0] == "w":
            white_pieces += 1
        if board[i][0] == "b":
            black_pieces += 1

    # Validating the number of found pieces.
    if white_pieces < 17 and black_pieces < 17:
        return True
    else:
        logging.debug("You have to many pieces.")
        return False


# Checking if each player has 8 pawns.
def checkPawnsNumber(board):

    # Counting pawns.
    white_pawns = 0
    black_pawns = 0

    # Adding up the pawns of each player found in the dictionary.
    for i in board.keys():
        if board[i][0] == "w" and board[i][1] == "P":
            white_pawns += 1
        if board[i][0] == "b" and board[i][1] == "P":
            black_pawns += 1

    # Validating the number of pawns.
    if white_pawns == 8 and black_pawns == 8:
        return True
    else:
        logging.debug("The number of pawns if incorrect.")
        return False


# Checking if all pieces are on valid squares from 'a1' to 'h8' etc.
def checkPiecesSquares(board):

    # Position is invalid until checked.
    white_pawns_position = False
    white_pieces_position = False

    black_pawns_position = False
    black_pieces_position = False

    # Checking white pawns position.
    for i in "abcdefgh":
        if board[i + str(2)] == "wP":
            white_pawns_position = True
        else:
            logging.debug("White pawns are not ok.")
            white_pawns_position = False
            break

    # Logging the result of white pawns check.
    if white_pawns_position:
        logging.debug("White pawns are ok.")

    # Checking the white pieces except pawns.
    if (
        board["a1"] == board["h1"] == "wR"
        and board["b1"] == board["g1"] == "wN"
        and board["c1"] == board["f1"] == "wB"
        and board["d1"] == "wQ"
        and board["e1"] == "wK"
    ):
        white_pieces_position = True
        logging.debug("White pieces are ok.")
    else:
        logging.debug("White pieces are not ok.")
        white_pieces_position = False

    # Checking black pawns position
    for i in "abcdefgh":
        if board[i + str(7)] == "bP":
            black_pawns_position = True
        else:
            logging.debug("Black pawns are not ok.")
            black_pawns_position = False
            break

    # Logging the result of black pawns check.
    if black_pawns_position:
        logging.debug("Black pawns are ok.")

    # Checking the black pieces except pawns.
    if (
        board["a8"] == board["h8"] == "bR"
        and board["b8"] == board["g8"] == "bN"
        and board["c8"] == board["f8"] == "bB"
        and board["d8"] == "bQ"
        and board["e8"] == "bK"
    ):
        black_pieces_position = True
        logging.debug("Black pieces are ok.")
    else:
        logging.debug("Black pieces are not ok.")
        black_pieces_position = False

    # Validating results.
    if (
        white_pawns_position
        and black_pawns_position
        and white_pieces_position
        and black_pieces_position
    ):
        logging.debug("Position is ok.")
        return True
    else:
        logging.debug("Something wrong in positioning.")
        return False


# Checking if piece names begin with either 'w' or 'b' and followed by a letter of a piece ('P', 'R', 'N', 'B', 'Q', 'K').
def checkPiecesNames(board):
    for i in board.values():
        # Checking the first letter: 'w' or 'b'.
        if i[0] != "w" and i[0] != "b":
            logging.debug("'w' or 'b' in names is incorrect.")
            return False

        # Checking the second letter: 'P', 'R', 'N', 'B', 'Q', 'K'.
        if (
            i[1] != "P"
            and i[1] != "R"
            and i[1] != "N"
            and i[1] != "B"
            and i[1] != "Q"
            and i[1] != "K"
        ):
            logging.debug("Something wrong with the wrong letter in the name.")
            return False
        else:
            # Returning True is everything is ok.
            logging.debug("Names are ok.")
            return True


BOARD_TEMPLATE = """
     a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = "||"
BLACK_SQUARE = "  "


def print_chessboard(board):
    squares = []
    is_white_square = True
    for y in "87654321":
        for x in "abcdefgh":
            if x + y in board.keys():
                squares.append(board[x + y])
            else:
                if is_white_square:
                    squares.append(WHITE_SQUARE)
                else:
                    squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square
    print(BOARD_TEMPLATE.format(*squares))


# Combining all the validations in one function.
def boardValidator(board):
    if (
        checkKings(board)
        and checkPiecesNumber(board)
        and checkPawnsNumber(board)
        and checkPiecesSquares(board)
        and checkPiecesNames(board)
    ):
        logging.debug("The board is ready!")
        return True


# If all validations are ok - proceed.
if boardValidator(STARTING_PIECES):

    print("Interactive Chessboard")
    print("by Al Sweigart al@inventwithpython.com")
    print()
    print("Pieces:")
    print(" w - White, b - Black")
    print(" P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King")
    print("Commands:")
    print(" move e2 e4 - Moves the piece at e2 to e4")
    print(" remove e2 - Removes the piece at e2")
    print(" set e2 wP - Sets square e2 to a white pawn")
    print(" reset - Resets pieces back to their starting squares")
    print(" clear - Clears the entire board")
    print(" fill wP - Fills entire board with white pawns.")
    print(" quit - Quits the program")

    main_board = copy.copy(STARTING_PIECES)
    while True:
        print_chessboard(main_board)
        response = input("> ").split()

        if response[0] == "move":
            main_board[response[2]] = main_board[response[1]]
            del main_board[response[1]]
        elif response[0] == "remove":
            del main_board[response[1]]
        elif response[0] == "set":
            main_board[response[1]] = response[2]
        elif response[0] == "reset":
            main_board = copy.copy(STARTING_PIECES)
        elif response[0] == "clear":
            main_board = {}
        elif response[0] == "fill":
            for y in "87654321":
                for x in "abcdefgh":
                    main_board[x + y] = response[1]
        elif response[0] == "quit":
            sys.exit()
