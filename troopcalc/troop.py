

class Troop(object):
    """A specific troop"""

    def __init__(self,name,type,buildTime,space,level,cost):
        self.__name = name
        self.__type = type
        self.__buildTime = buildTime
        self.__space = space
        self.__level = level
        self.__cost = cost

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

    @property
    def cost(self):
        return self.__cost

        
archer = Troop("archer","elixir","25s",1,1,400)
