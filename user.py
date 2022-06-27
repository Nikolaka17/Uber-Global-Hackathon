class User:
    def __init__(self, type, location):
        self.type = type
        self.local = location
        self.taken = False
    
    def pickup(self, passenger=None):
        self.taken = True
        if passenger is not None:
            passenger.pickup()
