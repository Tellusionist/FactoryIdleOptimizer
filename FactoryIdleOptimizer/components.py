class Conveyor:
    def __init__(self, level=1):
        i_per_tick = [2,3,4]
        self.value = 'c'
        self.level = level
        self.items = i_per_tick[level-1]
        

class Iron_Buyer:
    def __init__(self, level=1):
        ore_out = [2,4,8,12,24,36,48,64,96]
        self.value = 'ib'
        self.level = level
        self.output = ore_out[level-1]
        self.x = 2
        self.y = 2
        

class Iron_Foundry:
    def __init__(self, level=1):
        ore_in = [4,8,12,24,36,48,96,192]
        iron_out = [2,4,6,12,18,24,48,96]
        self.value = 'if'
        self.level = level
        self.output = iron_out[level-1]
        self.input = ore_in[level-1]
        self.x = 4
        self.y = 2

class Iron_Seller:
    def __init__(self, level=1):
        iron = [4,8]
        self.value = 'is'
        self.level = level
        self.sells = iron[level-1]
        self.x = 1
        self.y = 2