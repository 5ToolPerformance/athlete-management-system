from enum import Enum
from typing import Literal


class Position(str, Enum):
    """Player Postion"""

    FIRST_BASE = "1B"
    SECOND_BASE = "2B"
    THIRD_BASE = "3B"
    SHORTSTOP = "SS"
    LEFT_FIELD = "LF"
    CENTER_FIELD = "CF"
    RIGHT_FIELD = "RF"
    PITCHER = "P"
    CATCHER = "C"
    UTILITY = "U"


right_left = Literal["Right", "Left", "Switch"]
archetypes = Literal["Aerial", "Terrestrial"]
breath = Literal["In", "Out"]
association = Literal["Associated", "Disassociated"]
