import sys
import os
import pytest

# Get the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.insert(0, project_root)  # Add the root directory to sys.path

from src.Model.Knitting.Instructions.RibbingInstruction import RibbingInstruction


def test_():
    test_instruction = RibbingInstruction()
    print(test_instruction.get_instructions())

    assert "Cast on 150 stitches." == test_instruction.get_instructions()[0][0]
    assert 150 == test_instruction.get_instructions()[1]
