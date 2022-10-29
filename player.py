class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {'wood': 0, 'brick': 0, 'sheep': 0, 'wheat': 0, 'ore': 0}
        self.dev_cards = {'knight': 0, 'road building': 0, 'year of plenty': 0, 'monopoly': 0, 'vp': 0}
        self.settlements = []
        self.cities = []
        self.roads = []
        self.longest_road = 0
        self.victory_points = 0
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Player '" + self.name + "'>"
