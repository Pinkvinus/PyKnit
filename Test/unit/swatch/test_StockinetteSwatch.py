import sys
import os
import pytest

# Get the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.insert(0, project_root)  # Add the root directory to sys.path

print(sys.path)

from src.Model.Knitting.Swatches.StockinetteSwatch import StockinetteSwatch

def test_init_yarnid_non_positive_value():
    with pytest.raises(ValueError) as exc_info:
        StockinetteSwatch(-1,"3 mm", 1,1,1,1)
    assert str(exc_info.value) == "Swatch: yarnid has to be a non-negative number"

def test_init_stitches_non_positive_value():
    with pytest.raises(ValueError) as exc_info:
        StockinetteSwatch(1,"3 mm", -1,1,1,1)
    assert str(exc_info.value) == "Swatch: Stitches has to be a positive number"

def test_init_rows_non_positive_value():
    with pytest.raises(ValueError) as exc_info:
        StockinetteSwatch(1,"3 mm", 1,-1,1,1)
    assert str(exc_info.value) == "Swatch: Rows has to be a positive number"

def test_init_width_non_positive_value():
    with pytest.raises(ValueError) as exc_info:
        StockinetteSwatch(1,"3 mm", 1,1,-1,1)
    assert str(exc_info.value) == "Swatch: Width has to be a positive number"

def test_init_height_non_positive_value():
    with pytest.raises(ValueError) as exc_info:
        StockinetteSwatch(1,"3 mm", 1,1,1,-1)
    assert str(exc_info.value) == "Swatch: Height has to be a positive number"

def test_get_stitches_per_cm_():
    swatch = StockinetteSwatch(1, "3 mm", 1, 1, 1, 1)
    assert swatch.get_stitches_per_cm() == 1

def test_get_rows_per_cm_():
    swatch = StockinetteSwatch(1, "3 mm", 1, 1, 1, 1)
    assert swatch.get_rows_per_cm() == 1
