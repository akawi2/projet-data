class Ville:
    def __init__(self, x, y, id):
        self.id = id
        self.x = x
        self.y = y
        self.voisins = []
        
class Client:
    def __init__(self, ville, charge, open_time, close_time):
        self.ville = ville
        self.charge = charge
        self.open_time = open_time
        self.close_time = close_time
