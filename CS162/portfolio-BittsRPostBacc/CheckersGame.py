# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 03/15/2023
# Description: Two Players Checkers game

import numpy as np  # Necessary for the way I am creating the board


class OutofTurn(Exception):
    """
    Custom Exception for a player attempting to play when they shouldn't
    """
    pass


class InvalidSquare(Exception):
    """
    Custom Exception for a player attempting to move off of the board
    """
    pass


class InvalidPlayer(Exception):
    """
    Custom Exception for a player name that does not exist
    """
    pass


class Checkers:
    """
    Top Level of the Checkers Class
    """
    # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
    #   Not really any scenarios, but this is the Main Class for the game
    #   It handles top level player creation, game moves, board generation
    #       move tracking, winners and losers

    def __init__(self):
        """
        Default constructor for the Checkers class
        Initializes a game board on creation
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   Default constructor for the Checkers game class
        #   Generates a board and sets up needed objects for the game
        self._board = []
        spaces = 8
        for i in range(spaces):
            self._board.append(list(np.tile([None, "White"],
                                            int(spaces / 2))) if i % 2 == 0 else list(
                np.tile(["White", None], int(spaces / 2))))

        self._game_moves = {}
        self._current_players = []

    # TODO #1 * create_player -
    #  takes as parameter the player_name and piece_color that the player wants to play with
    #  and creates the player object. The parameter piece_color is a string of value "Black"
    #  or "White" representing Black or White checkers pieces respectively.
    #  This function returns the player object that has been created.
    def create_player(self, player_name, piece_color):
        """
        Function to create a player - interacts with the Player class
        :param player_name: the Name of the Player
        :param piece_color: the color the player wishes to choose
        :return: player object
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   Receive the player name and piece color
        #       check that the color is not already taken, and if not, assigns to that player,
        #       otherwise, returns "Color not available, assigning <the other color>"
        #   Check to ensure player name is not taken already, if so, ask for a different name
        #    Call the Player Class Create_Player function, write name and color choice to
        #       their respective Checkers.Players and Checkers.Colors lists, return Player object
        #   Function also updates the game board with the starting position of the pieces
        new_player = Player(player_name, piece_color)
        self._current_players.append(new_player)
        print(f"Current Players = {self._current_players}")
        self._board = Player.populate_game_board(new_player, self._board, piece_color)

    # TODO #2 * play_game -
    #  takes as parameter player_name, starting_square_location and
    #  destination_square_location of the piece that the player wants to move.
    #  The square_location is a tuple in format (x,y).
    #  If a player wants to move a piece from third square in the second row to fourth square
    #  in the fifth row, the starting and destination square locations will be (1,2) to (4,3).
    def play_game(self, player, starting_square, dest_square):
        """
        Function to "play game" - makes moves, captures pieces, Kings pieces
        :param player: Player name
        :param starting_square: coordinates of piece player wants to move
        :param dest_square: coordinates of where player wants to move to
        :return: Outcome of move - captures, Kings, or 0
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   Takes the players intended move, checks it for validity
        #           Is it their piece
        #           Is it a valid move
        #           Is the square they are moving to occupied
        #           Is it their turn
        #           Are they actually playing the correct game
        #   Did they capture a piece?  If so, return that
        #   Did they get promoted on side of the board or the other


    # TODO #2a-f Following the rules of the game move this piece.
    # TODO 2a - * If a player attempts to move a piece out of turn, raise an OutofTurn exception
    #     (you'll need to define this exception class).
    # TODO 2b - * If a player does not own the checker present in the square_location or if the
    #     square_location does not exist on the baord; raise an InvalidSquare exception
    #     (you'll need to define this exception class).
    # TODO 2c - * If the player_name is not valid, raise an InvalidPlayer exception
    #     (you'll need to define this exception class).
    # TODO 2d - * This method returns the number of captured pieces, if any, otherwise return 0.
    # TODO 2e - * If the destination piece reaches the end of opponent's side it is promoted as a
    #     king on the board. If the piece crosses back to its original side it becomes a triple king.
    # TODO 2f - * If the piece being moved is a king or a triple king assess the move according to
    #     the rules of the game.
    # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
    #   Check to ensure it is the players turn
    #   Verify the starting location is valid
    #   Verify the Player is valid
    #   Move the players piece according to the rules including King and Triple King rules
    #       Check to see if the opponent has a piece in destination, if so capture it, otherwise return 0
    #       If the move is the opponents base end, King players piece
    #       Otherwise if it the players base end, Triple King players piece

    # TODO #3 * get_checker_details -
    #  takes as parameter a square_location on the board and returns the checker details
    #  present in the square_location
    #     * Returns None, if no piece is present in the location
    #     * If the square_location does not exist on the board, raise an InvalidSquare
    #     exception (use the same exception class that was created for play_game function).
    #     * If black piece is present return "Black"
    #     * If white piece is present return "White"
    #     * If black king piece is present return "Black_king"
    #     * If white king piece is present return "White_king"
    #     * If black triple king piece is present return "Black_Triple_King"
    #     * If white triple king piece is present return "White_Triple_King"
    def get_checker_details(self, square_location):
        """
            Function to get details of a square and return the details so a move can be made
        :param square_location: Coordinates of the square to check
        :return: The results of the square check, if any, None other wise
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   Function to check the "contents" of a square
        #       Does the player have a piece there?  Does the Opponent?
        #       Return the color of the checker on that square if any
        #       Also return the type of piece if it is a King or Triple King
        #       If it's an invalid square, raise the InvalidSquare Exception

    # TODO #4 * print_board -
    #  takes no parameter, prints the current board in the form of an array.
    #  Below is an example showing the current board in the initial state
    #  (Note, here only the first row is printed, you would print the entire board)
    #   [[None, "White", None, "White", None, "White", None, "White"],....]

    def print_board(self):
        """
        Prints the current board in the form of an array.
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   Function print out the board, including where the pieces are on the board
        #   Board is blank when first created, updated on player creation and after every move
        row = []
        row_to_print = []
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                row.append(self._board[i][j])
            print(row)
            row = []

    # TODO #5 *game_winner -
    #  takes no parameter, returns the name of player who won the game.
    #   If the game has not ended, return "Game has not ended".
    #   In this function you need not check this condition -
    #   "A less common way to win is when all of your opponent's pieces are blocked so that
    #   your opponent can't make any more moves."
    def game_winner(self):
        """
        Function will determine if the player has won the game
        :return:
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   Function determines if the game has been won by a player after their turn
        #       I haven't really figured out the structure yet

class Player:
    """
    Class will handle player creation and statistics
    """

    def __init__(self, player, color):
        """
        Default constructor for the Player class
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   Default constructor for the Player class
        #       Class will handle player creation, and player statistics regarding
        #       promoted pieces, captured pieces and populates a new game board after
        #       a game is created
        # TODO #6 Player object represents the player in the game.
        #  It is initialized with player_name and checker_color that the player has chosen.
        #  The parameter piece_color is a string of value "Black" or "White".
        self._player_name = player
        self._checker_color = color

    # TODO #7 * get_king_count -
    #  takes no parameter, returns the number of king pieces that the player has
    def get_king_count(self):
        """

        :return:
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   Function will get the players promoted piece count
        #       I haven't really figured out the structure yet

    # TODO #8 * get_triple_king_count -
    #  takes no parameter, returns the number of triple king pieces that the player has
    def get_triple_king_count(self):
        """
        Function returns the players number of triple king pieces, if any
        :return: Count of Triple Kings
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   Function will get the players super promoted piece count
        #       I haven't really figured out the structure yet

    # TODO #9 * get_captured_pieces_count -
    #  takes no parameter, returns the number of opponent pieces that the player has captured
    def get_captured_pieces_count(self):
        """
        Function gets the players captured piece count
        :return: Number of pieces counted
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   Function will get the number of pieces that the player has captured
        #       I haven't really figured out the structure yet

    # TODO #10 - populate_game_board
    #   populate game board on player creation
    #   Takes color and updates game board
    def populate_game_board(self, board, color):
        """
        Function populates the game board
        :param color: color to place on the game board
        :param board: the current board
        :return: Nothing
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
        #   I hope to have this function Populate a game board after player creation
        #       so it is a work in progress.  Creating a board at game creation is fine, but
        #       I felt the board needed to be populated once the first player has been
        #       created
        updated_board = board
        if color.lower() == "black":
            row_num = 0
            for row in updated_board:
                if row_num < 2:
                    print(row)
                    # for space in row:
                    #     print(space)
                        # if space is None:
                            # updated_board[row_num] = str('Black')
                    res = [str(i or "Black") for i in row]
                    row = res
                    row_num += 1

        return updated_board


# For example, your classes will be used as below:


game = Checkers()
print(game.print_board())
Player1 = game.create_player("Adam", "White")
#
Player2 = game.create_player("Lucy", "Black")
print(game.print_board())
# game.play_game("Lucy", (5, 6), (4, 7))
#
# game.play_game("Adam", (2,1), (3,0))
#
# game.get_checker_details((3,1))
#
# Player1.get_captured_pieces_count()
