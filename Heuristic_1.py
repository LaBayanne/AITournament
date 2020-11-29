
import Goban

class Heuristic_1:

    def __init__(self):
        pass

    def eval(self, board, color):

        if(color == Goban.Board._BLACK):
            sign = 1
        else:
            sign = -1

        (black, white) = board.compute_score()

        #return sign * board._nbWHITE - sign * board._nbBLACK

        return black * sign - white * sign
    