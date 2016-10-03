
import pkg_resources
import pytest

import troopcalc.troopcreator
from troopcalc.troopcreator import TroopCreator

def test_makeTroops():
    """Test loading json and creating troop objects"""

    filePath = pkg_resources.resource_filename("troopcalc.data","test_troops.json")
    creator = TroopCreator(filePath)
    creator.makeTroops()
    assert "archer" in creator.troopCfgs
    assert len(creator.troopCfgs) == 12

def test_properties():
    """Test property accessors"""

    filePath = pkg_resources.resource_filename("troopcalc","../data/test_troops.json")
    creator = TroopCreator(filePath)
    assert creator.jsonFilePath == filePath
    with pytest.raises(AttributeError):
        creator.jsonFilePath = "foo"
    assert len(creator.troopCfgs) == 0
    with pytest.raises(AttributeError):
        creator.troopCfgs = {}
#    assert creator.getTroopCfg("archer") != none




