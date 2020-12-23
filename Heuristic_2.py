
import Goban

#Heuristique de milieu de partie (entre heuristique de début et de fin de partie)
class Heuristic_2:

    def __init__(self):
        pass

    def eval(self, board, color, move, player):
        poids = {"C3": 80, "C4": 80, "C5": 80, "C6": 80, "D3": 80, "D4": 80, "D5": 80, "D6": 80, "D7": 80,"E3": 80, "E4": 80, "E5": 80, "E6": 80, "E7": 80,"F3": 80, "F4": 80, "F5": 80, "F6": 80, "F7": 80, "G3": 80, "G4": 80, "G5": 80, "G6": 80, "G7": 80,
                 "B3": 60, "B4": 60, "B5": 60, "B6": 60, "B7": 60, "C2" : 60, "C7":60 , "C8":60, "D2":60 , "D8":60, "E2":60 , "E8":60, "F2":60 , "F8":60, "G2":60 , "G8":60, "H4":60, "H5":60 , "H6":60,"H7":60,
                 "B2":40, "B8":40, "H2":40, "H3":40, "H8":40,
                 "A2":20, "A3":20, "A4":20, "A5":20, "A6":20, "A7":20, "A8":20, "B1":20, "B9":20, "C1":20, "C9":20, "D1":20, "D9":20, "E1":20, "E9":20, "F1":20, "F9":20, "G1":20, "G9":20, "H1":20, "H9":20, "J2":20, "J3":20, "J4":20, "J5":20, "J6":20, "J7":20, "J8":20,
                 "A1":0, "A9":0, "J1":0, "J9":0 , "PASS":0}

        (black, white) = board.compute_score()

        black *= 10
        white *= 10

        if(player == 1):
            value = poids[board.flat_to_name(move)]
        else:
            value = -poids[board.flat_to_name(move)]

        if(color == Goban.Board._WHITE):
            sign = 1
            return (white + value) * sign - black * sign 
        else:
            sign = -1
            return white * sign - (black + value) * sign 