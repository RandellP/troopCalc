

#import troopcfg
from troopcalc.troopcfg import TroopCfg

costDict = {"1": 10, "2": 20}
tc = TroopCfg("archer","elixir",25,1,costDict)


import pkg_resources

from troopcalc.troopcreator import TroopCreator

def sayHi():
    print("hi from troopcalc")
#
#
filePath = pkg_resources.resource_filename("troopcalc.data","test_troops.json")
creator = TroopCreator(filePath)
creator.makeTroops()
creator.getTroopCfg("archer")
creator.getTroopCfg("foo")
