from typing import *
from utils import *
from common import *
from copy import deepcopy

class Cell:
    def __init__(self: Self,value: int) -> Self:
        
        if value not in VALID_VALUES:
            raise Exception("Not a valid value for sudoku cell")
        self.value = value
        self.initial_possibilities = [1,2,3,4,5,6,7,8,9]
        self.possibilities = deepcopy(self.initial_possibilities)
        self.given = True if value!=0 else False
        
    def set_initial_possibilities(self: Self,initial_possibilities : List[int]) -> None:
        self.initial_possibilities = deepcopy(initial_possibilities)
        self.possibilities = deepcopy(initial_possibilities)
    
    def get_initial_possibilities(self: Self) -> List[int]:
        return self.initial_possibilities
    
    def reset_to_initial_possibilities(self: Self) -> None:
        self.possibilities = deepcopy(self.initial_possibilities)
            
    def get(self: Self)-> int:
        return self.value
    
    def set(self: Self,value: int) -> None:
        self.value = value
    
    def get_possibilities(self: Self):
        return self.possibilities
    
    def set_possibilities(self: Self,possibilities: List[int]):
        self.possibilities = possibilities
        
    def add_possibilities(self: Self,possible: int):
        if possible not in self.possibilities:
            self.possibilities.append(possible)
    
    def remove_possibility(self: Self,not_possible: int):
        if not_possible in self.possibilities:
            self.possibilities.remove(not_possible)
    def nothing_possible(self: Self):
        return self.possibilities == [] 
    def is_empty(self: Self) -> bool:
        return self.value == 0
    
    def is_given(self: Self) -> bool:
        return self.given        
    def set_empty(self: Self) -> None:
        self.value = 0   
    
    def __repr__(self: Self) -> str:
        if self.value == 0:
            return colored("   ")
        else :
            if self.given:
                return colored(f" {self.value} ",fg = colors.fg.blue)
            else :
                return colored(f" {self.value} ",fg = colors.fg.red)
        
    
        
