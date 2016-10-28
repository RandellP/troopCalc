

class TroopCfg(object):
    "All the information needed to create a troop of any level"

    def __init__(self,name,type,buildTime,space,costArray):
        self.__name = name
        self.__type = type   #elixir or dark elixir
        self.__buildTime = buildTime  #in seconds
        self.__space = space
        self.__cost = costArray.copy()

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def buildTime(self):
        return self.__buildTime

    @property
    def space(self):
        return self.__space

    @property
    def level(self):
        return self.__level

    def costForLevel(self,level):
        return self.__cost[level - 1]
