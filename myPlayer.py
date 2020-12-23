# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
myPlayer class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import time
import Goban 
from random import choice
from playerInterface import *
from AlphaBeta import AlphaBeta

class myPlayer(PlayerInterface):
    ''' Example of a random player for the go. The only tricky part is to be able to handle
    the internal representation of moves given by legal_moves() and used by push() and 
    to translate them to the GO-move strings "A1", ..., "J8", "PASS". Easy!

    '''

    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None
        self._behavior = AlphaBeta()
        self._nbCoup = 0
        self._movePossible1 = {"B2", "C3", "G3", "H2", "A5", "J5", "B8", "H8", "D9", "F8"}
        self._movePossible2 = {"D2", "F2", "B5", "H5", "C7", "G7", "E8", "A4", "J4"}
        self._time = 0

    def getPlayerName(self):
        return "Floryannator"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS" 


        startTime = time.time()

        self._nbCoup += 1


        hasPassed = False

        if(self._board._lastPlayerHasPassed):
            (black, white) = self._board.compute_score()

            if(self._mycolor == Goban.Board._WHITE):
                if(white > black):
                    move = Goban.Board.name_to_flat("PASS")
                    hasPassed = True
            else:
                if(black > white):
                    move = Goban.Board.name_to_flat("PASS")
                    hasPassed = True


        if(not hasPassed):
            #Début de partie, soit avant nos 12 premiers coups, soit avant 24 pions de placés
            if self._board._nbBLACK + self._board._nbWHITE < 24:
                self._behavior.set_heuristic_start()

            #Milieu de partie, soit après nos 12 premiers coups, soit après 24 pions de placés
            if self._board._nbBLACK + self._board._nbWHITE > 24:
                self._behavior.set_heuristic_mid()

            #Fin de partie, soit 70% du plateau rempli, soit 56 pions placés
            if self._board._nbBLACK + self._board._nbWHITE > 56:
                self._behavior.set_heuristic_end()

            move = self._behavior.choose_move(self._board)



        self._board.push(move)
        
        self._time += time.time() - startTime
        print("My total time = " + str(self._time))


        # New here: allows to consider internal representations of moves
        print("I am playing ", self._board.move_to_str(move))
        print("My current board :")
        self._board.prettyPrint()
        # move is an internal representation. To communicate with the interface I need to change if to a string

        return Goban.Board.flat_to_name(move) 

    def playOpponentMove(self, move):
        print("Opponent played ", move) # New here
        # the board needs an internal represetation to push the move.  Not a string
        move = Goban.Board.name_to_flat(move)
        self._board.push(move) 

    def newGame(self, color):
        self._mycolor = color
        self._opponent = Goban.Board.flip(color)

        self._behavior._color = self._mycolor

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")



