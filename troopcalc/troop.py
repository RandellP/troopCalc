
class Troop(object):
    "A specific troop of a specific level"

    def __init__(self,troopCfg,level):
        self.__troopCfg = troopCfg
        self.__level = level

    @property
    def name(self):
        return self.__troopCfg.name

    @property
    def type(self):
        return self.__troopCfg.type

    @property
    def buildTime(self):
        return self.__troopCfg.buildTime

    @property
    def space(self):
        return self.__troopCfg.space

    @property
    def level(self):
        return self.__troopCfg.level

    @property
    def cost(self):
        return self.__troopCfg.costForLevel(self.__level)


