class Skill():
    def __init__(self):
        self.actionID = 2 #normal attack
        self.range = 50
        self.direction = "forward"

class Empty(Skill):
    def __init__(self):
        Skill().__init__()
        self.actionID = 1

class Attack(Skill):
    def __init__(self):
        Skill().__init__()

class Explosion(Skill):
    def __init__(self):
        Skill().__init__()
        self.actionID = 3
        self.range = 200
        self.direction = "all"
