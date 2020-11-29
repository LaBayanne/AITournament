# -*- coding: utf-8 -*-

import time
import Goban
import numpy as np
from Heuristic_1 import Heuristic_1

class AlphaBeta:

    def __init__(self, color):
        self._heuristic = Heuristic_1()
        self._color = color
        self.timeExe = 0
        self.time = 0
        self.timeToExe = 0.5
        self.diffTime = 0.01

    def choose_move(self, board):

        self.time = time.time()
        self.timeExe = 0
        maxDepth = 1

        bestMove = None

        alpha = -np.inf
        beta = np.inf

        while(self.timeExe < self.timeToExe - self.diffTime):
            
            newMove = self.get_best_move(board, alpha, beta, maxDepth)
            if(newMove == None):
                break
            bestMove = newMove
            maxDepth += 1

        if(bestMove == None):
            print("Yolo\n")
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

            newScore = self.minNode(board, alpha, beta, h - 1)
            board.pop()

            if(newScore == None):
                return None

            newScore = max(score, newScore)

            if(newScore > score):
                bestMove = move
                score = newScore

            if(alpha >= beta):
                return bestMove
                
            alpha = max(alpha, score)

        return bestMove

    def maxNode(self, board, alpha, beta, h):

        print("Max",end='')

        tmpTime = time.time()
        self.timeExe += time.time() - self.time
        self.time = tmpTime
        if(self.timeExe >= self.timeToExe - self.diffTime):
            return None

        if board.is_game_over() or h == 0:
            return self._heuristic.eval(board, self._color)

        score = -np.inf

        for move in board.weak_legal_moves():
            while True:
                valid = board.push(move)
                if valid:
                    break
                board.pop()

            newScore = self.minNode(board, alpha, beta, h - 1)
            board.pop()

            if(newScore == None):
                return None

            score = max(score, newScore)

            if(alpha >= beta):
                return score

            alpha = max(alpha, score)            
            
        return score

    def minNode(self, board, alpha, beta, h):

        print("Min", end='')

        tmpTime = time.time()
        self.timeExe += time.time() - self.time
        self.time = tmpTime
        if(self.timeExe >= self.timeToExe - self.diffTime):
            return None

        if board.is_game_over() or h == 0:
            return self._heuristic.eval(board, self._color)

        score = np.inf

        for move in board.weak_legal_moves():
            while True:
                valid = board.push(move)
                if valid:
                    break
                board.pop()

            newScore = self.maxNode(board, alpha, beta, h - 1)
            board.pop()

            if(newScore == None):
                return None

            score = min(score, newScore)

            if(alpha >= beta):
                return score

            beta = min(beta, score)


        return score
