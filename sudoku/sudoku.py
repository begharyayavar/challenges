from typing import *
from cell import *
from rules import *
import time
import os
from copy import deepcopy
class Sudoku:
    def __init__(self,sudoku: List[List[int]]) -> Self:
        self.sudoku = [[Cell(i) for i in j] for j in sudoku]
        self.rules = Rules(DEFAULT_RULES)
        
        self.size_X = len(sudoku[0])
        self.size_Y = len(sudoku)
        self.iterations = 0
        
        self.set_initial_possibilities()
        
        self.solved = False
        # self.show_initial_possibilities()

    def set_initial_possibilities(self: Self) -> None:
        for i in VALID_INDEXES:
            for j in VALID_INDEXES:

                current_cell = self.get_cell((i,j))

                if not current_cell.is_given():
                    current_cell.set_initial_possibilities(self.check_possibility((i,j)))
                    
    def show_initial_possibilities(self: Self) -> None:
        for i in VALID_INDEXES:
            for j in VALID_INDEXES:
                current_cell = self.get_cell((i,j))
                if not current_cell.is_given():
                    print(f"initial_possibilities {i} {j}: {current_cell.get_possibilities()}")
                    
    
    def iterate(self: Self)-> int:
        print(self.iterations,end="")
        print("\b\b\b\b\b\b\b\b\b",end="")
        self.iterations += 1
        
    def reset_iteration(self: Self) ->int:
        current_iterations = self.iterations
        self.iteration = 0
        return current_iterations
        
    def solve_smart(self: Self) -> None:
        # TOUCH VERY CAREFULLY
        self.iterate()
        
        
        # if self.iterations % 1000 == 0:
        #     self.draw()
        
        for i in VALID_INDEXES:
            for j in VALID_INDEXES:

                current_cell = self.get_cell((i,j))
                
                if not current_cell.is_given():

                    if current_cell.is_empty() :                    

                        possibilities = deepcopy(current_cell.get_possibilities())                        
                        
                        is_something_possible = False
        
                        for k in possibilities:
                            current_cell.set_empty()
                            if self.check_possibility_cell_value((i,j),k):
                                is_something_possible = True
                                current_cell.set(k)
                                self.solve_smart()
                                if self.is_solved():
                                    return
                                
                        if self.check_is_solved():
                            print(f"solved = {self.solved}")
                            return 
                        
                        if not is_something_possible or not self.is_solved():
                            current_cell.set_empty()
                            return
                            
    def get_cell(self: Self,index :tuple[int,int]) -> Cell:
        if index[0] not in VALID_INDEXES or index[1] not in VALID_INDEXES:
            raise Exception("Invalid Index Given (Base 1 indexing used)")
        return self.sudoku[index[0]-1][index[1]-1]   
    
    def get_row(self: Self ,index_row: int) -> List[Cell]:
        return self.sudoku[index_row-1]
        
    def get_column(self: Self,index_column: int) -> List[Cell]:
        pass
        
    def get_3x3(self: Self,index_3x3: tuple[int,int]) -> List[Cell]:    
        pass
        
            
    def check_all_possibilities(self: Self) -> None:
        for i in VALID_INDEXES:
            for j in VALID_INDEXES:
                self.check_possibility((i,j))
    
    def check_possibility(self,index : tuple[int,int]) -> List[int]:
        possibilities = []
        for i in [1,2,3,4,5,6,7,8,9]:
            passed : bool = self.check_possibility_cell_value(index,i)
            if passed:
                possibilities.append(i)
        return possibilities
    
    def check_possibility_cell_value(self,index : tuple[int,int],value: int) -> bool:
        passed_checks = []
        for rule in self.rules.get_rules():
            current_rule = self.rules.get_rule(rule)
            collection_of_indexes = current_rule.get_pattern().get()[(index[0],index[1])]
            collection_of_values = [self.get_cell((i[0],i[1])).get() for i in collection_of_indexes]
            passed_checks.append(current_rule.check(collection_of_values,value))
        return all(passed_checks)
            
    def is_solved(self: Self) -> bool:
        return self.solved
    
    def solved(self: Self) -> bool:
        self.solved = True
        return self.solved
    def check_is_solved(self: Self) -> bool:
        for i in VALID_INDEXES:
            for j in VALID_INDEXES:
                current_cell = self.get_cell((i,j))
                if current_cell.is_empty():
                    return False
                for rule in self.rules.get_rules():
                    current_rule = self.rules.get_rule(rule)
                    collection_of_indexes = current_rule.get_pattern().get()[(i,j)]
                    collection_of_values = [self.get_cell((i[0],i[1])).get() for i in collection_of_indexes]
                    if not current_rule.check(collection_of_values,current_cell):
                        self.draw()
                        return False
        self.solved = True
        print("SOLVED!!!")
        return True    
    """
    def draw(self: Self,mode :str = "complete") -> None:
        self.draw_blank()
        match mode:
            case "complete":
                for i in inclusive_range(1,self.size_Y):
                    print(colored(f"- - - - - - - " *3))
                    print(colored(f"||"),end = "")
                    for j in inclusive_range(1,self.size_X):
                        print(f"{self.get_cell((i,j))}",end = "")
                        if j%3 == 0:
                            print(colored(f"|"),end = "")
                        print(colored(f"|"),end = "")
                    print(colored(" "))
                    if i%3 == 0:
                        print(colored(f"- - - - - - - " *3))
                    print(f"{colors.reset}",end="")
                
            case " 3x3":
                pass
        self.draw_blank()
        time.sleep(2)
    
    def draw_blank(self: Self) -> None:
        print(colored("",bg = colors.bg.black))        
    """    
