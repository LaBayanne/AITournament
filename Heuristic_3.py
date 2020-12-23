import Goban

#Heuristique de fin de partie (quand le plateau de jeu est rempli à 70%)
class Heuristic_3:

    def __init__(self):
        pass

    def eval(self, board, color, move, player):
        poids = {"A4":60, "A5":60, "A6":60, "C2" : 60, "F1":60, "J5":60,  
                "A3":40, "A7":40, "A8":40, "B1":40, "B2":40, "B3": 40, "B4": 40, "B5": 40,  "B6": 40, "B7": 40, "B8":40, "B9":40, "C1":40, "C9":40, "D1":40, "D2":40, "D5": 40, "D6": 40, "D9":40, "E1":40, "E8":40, "E9":40, "F2":40, "F8":40, "F9":40, "G1":40, "G2":40, "G9":40, "H1":40,  "H2":40,  "H4":40, "H5":40 , "H6":40,"H7":40, "H8":40, "J4":40, "J6":40, "J7":40,  
                "A2":20, "C3": 20, "C4": 20, "C5": 20, "C7":20, "C8":20, "D3": 20, "D4": 20, "D8":20, "E2":20, "E4": 20, "E6": 20, "F3": 20, "F4": 20, "F5": 20, "F6": 20, "F7": 20, "G3": 20, "G5": 20, "G6": 20, "G7": 20, "G8":20, "H3":20, "H9":20, "J2":20, "J3":20, "J8":20, 
                "A1":0, "A9":0, "C6": 0, "D7": 0, "E3": 0, "E5": 0, "E7": 0, "G4": 0, "J1":0, "J9":0, 
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