import Goban

#Heuristique de début de partie (12 premiers coups)
class Heuristic_1:

    def __init__(self):
        pass

    def eval(self, board, color, move, player):
        poids = {"E5": 60,
                "C3": 40, "C4": 40, "C5": 40, "C6": 40, "C7":40 , "D3": 40, "D4": 40, "D5": 40, "D6": 40, "D7": 40,"E3": 40, "E4": 40, "E6": 40, "E7": 40,"F3": 40, "F4": 40, "F5": 40, "F6": 40, "F7": 40, "G3": 40, "G4": 40, "G5": 40, "G6": 40, "G7": 40,
                 "B5": 20, "D2":20 , "D8":20, "E2":20 , "E8":20, "F2":20, "F8":20, "H3":20, "H4":20, "H5":20 , "H6":20,
                 "A1":0, "A2":0, "A3":0, "A4":0, "A5":0, "A6":0, "A7":0, "A8":0, "A9":0, "B1":0, "B2":0, "B3": 0, "B4": 0, "B6": 0, "B7": 0, "B8":0, "B9":0, "C1":0, "C2" : 0,  "C8":0, "C9":20, "D1":0, "D9":0, "E1":0, "E9":0, "F1":0, "F9":0, "G1":0, "G2":0 , "G8":0, "G9":0, "H1":0,  "H2":0,  "H7":0, "H8":0, "H9":0, "J1":0, "J2":0, "J3":0, "J4":0, "J5":0, "J6":0, "J7":0, "J8":0, "J9":0, 
                 "PASS":0}

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