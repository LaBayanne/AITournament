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
        self.timeExe = 0
        self.time = 0
        self.timeToExe = 1
        self.diffTime = 0.01

    def set_heuristic_start(self):
        self._heuristic = Heuristic_1()
        self.timeToExe = 0.5

    def set_heuristic_mid(self):
        self._heuristic = Heuristic_2()
        self.timeToExe = 5

    def set_heuristic_end(self):
        self._heuristic = Heuristic_3()
        self.timeToExe = 3

    def choose_move(self, board):

        self.time = time.time()
        self.timeExe = 0
        maxDepth = 1

        bestMove = None

        alpha = -np.inf
        beta = np.inf

        while(self.timeExe < self.timeToExe - self.diffTime):
            
            newMove = self.get_best_move(board, alpha, beta, maxDepth)

            print("_________________________________________________")
            if(newMove == None):
                break
            bestMove = newMove
            maxDepth += 2

        if(bestMove == None):
            bestMove = board.legal_moves()[0]
        
        tmpTime = time.time()
        self.timeExe += time.time() - self.time
        self.time = tmpTime

        print("----------")

        print("Iterative deepening depth : " + str(maxDepth))
        print("Research time : " + str(self.timeExe))

        return bestMove

    def get_best_move(self, board, alpha, beta, h):

        tmpTime = time.time()
        self.timeExe += time.time() - self.time
        self.time = tmpTime
        if(self.timeExe >= self.timeToExe - self.diffTime):
            return None

        score = -np.inf
        bestMove = None

        for move in board.weak_legal_moves():
            while True:
                valid = board.push(move)
                if valid:
                    break
                board.pop()

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

        return bestMove

    def maxNode(self, board, alpha, beta, h, move):

        tmpTime = time.time()
        self.timeExe += time.time() - self.time
        self.time = tmpTime
        if(self.timeExe >= self.timeToExe - self.diffTime):
            return None

        if board.is_game_over() or h == 0:
            return self._heuristic.eval(board, self._color, move, 2)

        score = -np.inf

        for move in board.weak_legal_moves():
            while True:
                valid = board.push(move)
                if valid:
                    break
                board.pop()

            newScore = self.minNode(board, alpha, beta, h - 1, move)
            board.pop()

            if(newScore == None):
                return None

            score = max(score, newScore)

            alpha = max(alpha, score)  

            if(alpha >= beta):
                return score

            
        return score

    def minNode(self, board, alpha, beta, h, move):

        tmpTime = time.time()
        self.timeExe += time.time() - self.time
        self.time = tmpTime
        if(self.timeExe >= self.timeToExe - self.diffTime):
            return None

        if board.is_game_over() or h == 0:
            return self._heuristic.eval(board, self._color, move, 1)

        score = np.inf

        for move in board.weak_legal_moves():
            while True:
                valid = board.push(move)
                if valid:
                    break
                board.pop()

            newScore = self.maxNode(board, alpha, beta, h - 1, move)
            board.pop()

            if(newScore == None):
                return None

            score = min(score, newScore)

            beta = min(beta, score)

            if(alpha >= beta):
                return score



        return score
