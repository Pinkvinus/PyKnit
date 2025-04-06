
from src.Model.Knitting.Instructions.ShapingInstruction import ShapingInstruction


def test_ShapingInstruction_init_positive_values():
    test_instruction = ShapingInstruction(1,2,3,4,"")
    assert test_instruction.order == 4
    
def test_ShapingInstruction_str():
    test_instruction = ShapingInstruction(1,2,3,4,"None")
    assert str(test_instruction) == "Number of rows: 1, initial number of stitches: 2, Terminal number of stitches: 3 Order: 4, Advanced instructions: None"