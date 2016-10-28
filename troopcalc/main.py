

##import troopcfg
#from troopcalc.troopcfg import TroopCfg
#
#costDict = {1: 10, 2: 20}
#tc = TroopCfg("archer","elixir",25,1,costDict)
#
#

import pkg_resources

from troopcalc.troopcreator import TroopCreator
from troopcalc.troop import Troop

def sayHi():
    print("hi from troopcalc")


def doIt():
  filePath = pkg_resources.resource_filename("troopcalc.data","troops.json")
  creator = TroopCreator(filePath)
  creator.loadTroopCfgs()
  archerCfg = creator.getTroopCfg("archer")
  archer = Troop(archerCfg,1)
  cost = archer.cost
  print(cost)

if __name__ == "__main__":
  doIt()




