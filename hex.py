import random


class Hex:
    hexes = []
    types = ['desert', 'water', 'harbor', 'wood', 'brick', 'sheep', 'wheat', 'ore']
    instantiated = {'desert': 0, 'water': 0, 'harbor': 0, 'wood': 0, 'brick': 0, 'sheep': 0, 'wheat': 0, 'ore': 0}

    def __init__(self, type):
        assert type in Hex.types
        self.type = type
        Hex.hexes.append(self)
        Hex.instantiated[type] += 1

    def generate_random_resource_hex():
        return ResourceHex()

    def generate_random_harbor_hex():
        return HarborHex()

    def generate_water_hex():
        return WaterHex()

    def generate_desert_hex():
        return DesertHex()

    def draw_hex(self):
        pass

    def __str__(self):
        if self.type in ResourceHex.resource_types:
            return self.type + " - " + str(self.number)
        return self.type

    def __repr__(self):
        return self.__str__()


class ResourceHex(Hex):
    resource_hexes = []
    chit_numbers = [5, 10, 8, 2, 9, 3, 4, 6, 11, 6, 11, 3, 4, 5, 12, 8, 10, 9]
    resource_types = ['wood', 'brick', 'sheep', 'wheat', 'ore']

    def __init__(self):
        self.type = ResourceHex.get_random_type()
        self.number = ResourceHex.chit_numbers[len(ResourceHex.resource_hexes)]
        super().__init__(self.type)
        self.resource_hexes.append(self)

    def get_random_type():
        random_number = random.randint(0, len(ResourceHex.resource_types) - 1)
        type = ResourceHex.resource_types[random_number]
        existing_hexes_of_type = Hex.instantiated[type]

        if (type == 'wood' or type == 'wheat' or type == 'sheep') and existing_hexes_of_type == 4:
            return ResourceHex.get_random_type()
        elif (type == 'ore' or type == 'brick') and existing_hexes_of_type == 3:
            return ResourceHex.get_random_type()
        return type


class DesertHex(Hex):
    def __init__(self):
        super().__init__('desert')


class HarborHex(Hex):
    trade_resources = ['any', 'wood', 'brick', 'sheep', 'wheat', 'ore']
    harbors_instantiated = {'any': 0, 'wood': 0, 'brick': 0, 'sheep': 0, 'wheat': 0, 'ore': 0}
    harbors_remaining = {'any': 4, 'wood': 1, 'brick': 1, 'sheep': 1, 'wheat': 1, 'ore': 1}

    def __init__(self):
        super().__init__('harbor')
        self.trade_resource = HarborHex.get_random_trade_resource()
        HarborHex.harbors_instantiated[self.trade_resource] += 1
        HarborHex.harbors_remaining[self.trade_resource] -= 1

    def get_random_trade_resource():
        random_int = random.randint(0, len(HarborHex.trade_resources) - 1)
        resource = HarborHex.trade_resources[random_int]
        if HarborHex.harbors_remaining[resource] == 0:
            return HarborHex.get_random_trade_resource()
        return resource


class WaterHex(Hex):
    def __init__(self):
        super().__init__('water')