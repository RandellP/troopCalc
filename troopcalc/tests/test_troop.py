
import pytest
from troopcalc.troopcfg import TroopCfg
from troopcalc.troop import Troop

def test_properties():
    """Test property accessors"""
    cost = {"1": 50, "2": 80}
    archerCfg = TroopCfg("archer","elixir",25,1,cost)
    archer = Troop(archerCfg,"2")

    assert archer.name == "archer"
    assert archer.type == "elixir"
    assert archer.buildTime == 25
    assert archer.space == 1
    assert archer.cost == 80
    with pytest.raises(AttributeError):
        archer.name = "junk"
    with pytest.raises(AttributeError):
        archer.type = "junk"
    with pytest.raises(AttributeError):
        archer.buildTime = "junk"
    with pytest.raises(AttributeError):
        archer.space = "junk"
    with pytest.raises(AttributeError):
        archer.cost = cost


