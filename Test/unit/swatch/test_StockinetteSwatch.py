import sys
import os
import pytest

# Get the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.insert(0, project_root)  # Add the root directory to sys.path

print(sys.path)

from src.Model.Knitting.Swatches.StockinetteSwatch import StockinetteSwatch


def test_StockinetteSwatch_get_stitches_per_cm_():
    swatch = StockinetteSwatch(1, "3 mm", 1, 1, 1, 1)
    assert swatch.get_stitches_per_cm() == 1
