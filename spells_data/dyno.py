stone = "olivine"

kind = "summon"

name = "Dyno"

description = "Summon a Dyno"

speed = 5

requirements = None

def summon_dyno(status, dyno):
    dyno = monsters.Monster(status)
    
    dyno.HP = 20
    dyno.MP = 50
    dyno.TP = 0
    dyno.ATK = 20
    dyno.DEF = 10
    dyno.MATK = 5
    dyno.MDEF = 5
    dyno.DEX = 10
    dyno.LUK = 1
    
    dyno.dead = False
    dyno.burnt = 0
    dyno.poisoned = 0
    dyno.frozen = 0
    dyno.paralyzed = 0
        
    status.party.add(dyno)

effect = summon_dyno
