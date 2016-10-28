

import json

from troopcalc.troopcfg import TroopCfg

class TroopCreator(object):
    "Creates and handles Troop objects"

    def __init__(self,jsonFilePath):
        self.__jsonFilePath = jsonFilePath
        self.__troopCfgs = {}

    @property
    def jsonFilePath(self):
        return self.__jsonFilePath

    @property
    def troopCfgs(self):
        return self.__troopCfgs

    def loadTroopCfgs(self):
        fileData = open(self.__jsonFilePath).read()
        jsonData = json.loads(fileData)
        troopArray = jsonData["troops"]
        for troopDef in troopArray:
            name = troopDef["name"]   
            self.__troopCfgs[name] = TroopCfg(name,troopDef["type"],troopDef["buildTime"],troopDef["housingSpace"],troopDef["buildCost"])


    def getTroopCfg(self,name):
      return(self.__troopCfgs.get(name)) #return none if doesn't exist instead of raising an expection



#import pkg_resources
#filePath = pkg_resources.resource_filename("troopcalc.data","test_troops.json")
#creator = TroopCreator(filePath)
#creator.makeTroops()
#creator.getTroopCfg("archer")
#creator.getTroopCfg("foo")
