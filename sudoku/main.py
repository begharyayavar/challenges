from imports import *

puzzle = parse_sudoku("puzzle5.csv")

sudoku = Sudoku(puzzle)

# sudoku.draw()

sudoku.solve_smart()

print("---------------------------------------------------")
# sudoku.draw()

print(sudoku.iterations)
