# -*- coding: utf-8 -*-

import time
import Goban
import numpy as np
from Heuristic_1 import Heuristic_1
from Heuristic_2 import Heuristic_2
from Heuristic_3 import Heuristic_3

class AlphaBeta:

    def __init__(self):
        self._heuristic = Heuristic_1()
        self._color = None
        self._timeExe = 0
        self._time = 0
        self._timeToExe = 1
        self._diffTime = 0.01

    def set_heuristic_start(self):
        self._heuristic = Heuristic_1()
        self._timeToExe = 0.5

    def set_heuristic_mid(self):
        self._heuristic = Heuristic_2()
        self._timeToExe = 5

    def set_heuristic_end(self):
        self._heuristic = Heuristic_3()
        self._timeToExe = 3

    def choose_move(self, board):

        self._time = time.time()
        self._timeExe = 0
        maxDepth = 1

        bestMove = None

        alpha = -np.inf
        beta = np.inf

        while(self._timeExe < self._timeToExe - self._diffTime):
            
            newMove = self.get_best_move(board, alpha, beta, maxDepth)

            if(newMove == None):
                break
            bestMove = newMove
            maxDepth += 2

        if(bestMove == None):
            bestMove = board.legal_moves()[0]
        
        tmpTime = time.time()
        self._timeExe += time.time() - self._time
        self._time = tmpTime

        print("----------")

        print("Iterative deepening depth : " + str(maxDepth))
        print("Research time : " + str(self._timeExe))

        return bestMove

    def get_best_move(self, board, alpha, beta, h):

        tmpTime = time.time()
        self._timeExe += time.time() - self._time
        self._time = tmpTime
        if(self._timeExe >= self._timeToExe - self._diffTime):
            return None

        score = -np.inf
        bestMove = None

        for move in board.weak_legal_moves():
            valid = board.push(move)
            if valid:

                newScore = self.minNode(board, alpha, beta, h - 1, move)
                board.pop()

                if(newScore == None):
                    return None

                if(newScore > score):
                    bestMove = move
                    score = newScore

                if(score >= beta):
                    return bestMove
                    
                alpha = max(alpha, score)
            else:
                board.pop()

        return bestMove

    def maxNode(self, board, alpha, beta, h, move):

        tmpTime = time.time()
        self._timeExe += time.time() - self._time
        self._time = tmpTime
        if(self._timeExe >= self._timeToExe - self._diffTime):
            return None

        if board.is_game_over() or h == 0:
            return self._heuristic.eval(board, self._color, move, 2)

        score = -np.inf

        for move in board.weak_legal_moves():
            valid = board.push(move)
            if valid:

                newScore = self.minNode(board, alpha, beta, h - 1, move)
                board.pop()

                if(newScore == None):
                    return None

                score = max(score, newScore)

                alpha = max(alpha, score)  

                if(alpha >= beta):
                    return score
            else:
                board.pop()

            
        return score

    def minNode(self, board, alpha, beta, h, move):

        tmpTime = time.time()
        self._timeExe += time.time() - self._time
        self._time = tmpTime
        if(self._timeExe >= self._timeToExe - self._diffTime):
            return None

        if board.is_game_over() or h == 0:
            return self._heuristic.eval(board, self._color, move, 1)

        score = np.inf

        for move in board.weak_legal_moves():
            valid = board.push(move)
            if valid:

                newScore = self.maxNode(board, alpha, beta, h - 1, move)
                board.pop()

                if(newScore == None):
                    return None

                score = min(score, newScore)

                beta = min(beta, score)

                if(alpha >= beta):
                    return score
            else:
                board.pop()



        return score
