from defaults import *
from typing import *

def inclusive_range(i : int = 0,j : int = 9,increment : int = 1):
    return range(i,j+1,increment)

def colored(string: str,bg :colors.bg = DEFAULT_BG_COLOR,fg : colors.fg = DEFAULT_FG_COLOR,bold = True) -> str:
    return f"{bg}{fg}{colors.bold if bold else ""}{string}{colors.reset}"

def nearest_multiple_of_three_floor(value: int)-> int:
    return value - value%3

def nearest_multiple_of_three_ceil(value: int)-> int:
    return value + (3 - value%3)

def parse_sudoku(filename: str) -> List[List[int]]:
    sudoku = []
    with open(filename,'r') as f:
        for line in f:
            sudoku.append(list(map(int,line.strip().split(','))))
    return sudoku

