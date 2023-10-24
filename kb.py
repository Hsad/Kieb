# RIGHT
import board

from kmk.modules.split import SplitSide

class varList():
    col_pins = (
        board.D0,
        board.D1,
        board.D2,
        board.D3,
        board.D10,
    )

    row_pins = (
        board.D4,
        board.D5,
        board.D8,
        board.D9,
    )

    ss = SplitSide.RIGHT
