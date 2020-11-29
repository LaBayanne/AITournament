# -*- coding: utf-8 -*-

import time
import Goban
import numpy as np
from Heuristic_1 import Heuristic_1

class AlphaBeta:

    def __init__(self, color):
        self._heuristic = Heuristic_1()
        self._color = color

    def get_best_move(self, board):

        bestMove = None

        score = np.inf
        alpha = -np.inf
        beta = np.inf
        h = 3

        for move in board.weak_legal_moves():
            while True:
                valid = board.push(move)
                if valid:
                    break
                board.pop()

            newScore = max(score, self.minNode(board, alpha, beta, h - 1))
            board.pop()

            if(newScore >= score):
                bestMove = move
                score = newScore

            if(alpha >= beta):
                return bestMove
                
            alpha = max(alpha, score)

        
        return bestMove

    
    def maxNode(self, board, alpha, beta, h):

        if board.is_game_over() or h == 0:
            return self._heuristic.eval(board, self._color)

        score = -np.inf

        for move in board.weak_legal_moves():
            while True:
                valid = board.push(move)
                if valid:
                    break
                board.pop()

            score = max(score, self.minNode(board, alpha, beta, h - 1))
            board.pop()

            if(alpha >= beta):
                return score

            alpha = max(alpha, score)            
            
        return score

    def minNode(self, board, alpha, beta, h):

        if board.is_game_over() or h == 0:
            return self._heuristic.eval(board, self._color)

        score = np.inf

        for move in board.weak_legal_moves():
            while True:
                valid = board.push(move)
                if valid:
                    break
                board.pop()

            score = min(score, self.maxNode(board, alpha, beta, h - 1))
            board.pop()

            if(alpha >= beta):
                return score

            beta = min(beta, score)


        return score
