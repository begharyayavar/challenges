from typing import *
from common import *
from utils import *

def generate_pattern_row():
    return {(i,j):[(i,k) for k in VALID_INDEXES] for i in VALID_INDEXES for j in VALID_INDEXES}     

def generate_pattern_column():
    return {(i,j):[(k,j) for k in VALID_INDEXES] for i in VALID_INDEXES for j in VALID_INDEXES}

def generate_pattern_3x3():
    return {(i,j):[\
                    (h,k) \
                        for h in inclusive_range(nearest_multiple_of_three_floor(i-1) + 1,nearest_multiple_of_three_ceil(i-1)) \
                            for k in inclusive_range(nearest_multiple_of_three_floor(j-1) + 1,nearest_multiple_of_three_ceil(j-1)) \
                    ] for i in VALID_INDEXES for j in VALID_INDEXES}

class Pattern:
    def __init__(self: Self,type : str) -> Self:
        match type:
            case "row":
                self.pattern = generate_pattern_row()
            case "column":
                self.pattern = generate_pattern_column()
            case "3x3":
                self.pattern = generate_pattern_3x3()
            case _:
                raise Exception("Unknown Pattern Type")
    
    def get(self: Self) -> Dict:
        return self.pattern


# print(generate_pattern_row())
# print(generate_pattern_column())
# print(generate_pattern_3x3())
