import sys
import os
import pytest

# Get the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.insert(0, project_root)  # Add the root directory to sys.path

from src.Model.Knitting.Instructions.ShapingInstruction import ShapingInstruction


def test_instruction_init_positive_values():
    test_instruction = ShapingInstruction(1,2,3,4,"")
    assert test_instruction.num_rows == 1
    assert test_instruction.start_stitches == 2
    assert test_instruction.end_stitches == 3

def test_instruction_init_negative_values():
    with pytest.raises(ValueError) as exc_info:
        ShapingInstruction(-1,1,1,1,"")
    assert str(exc_info.value) == "Instruction can't be initialised with negative values"
    with pytest.raises(ValueError) as exc_info:
        ShapingInstruction(1,-1,1,1,"")
    assert str(exc_info.value) == "Instruction can't be initialised with negative values"
    with pytest.raises(ValueError) as exc_info:
        ShapingInstruction(1,1,-1,1,"")
    assert str(exc_info.value) == "Instruction can't be initialised with negative values"
