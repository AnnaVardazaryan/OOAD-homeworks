from Cell import Cell
from copy import deepcopy

class Spreadsheet:
    def __init__(self, rows, columns):
        if rows > 0 and columns > 0 and isinstance(rows, int) and isinstance(columns, int):
            self._shape1 = rows
            self._shape2= columns
            self.spreadsheet = [[Cell() for j in range(columns)] for i in range(rows)]
        else:
            print("Initialize spreadsheet with valid shapes")

    def set_cell_at(self, row, col, c):
        if row in range(self._shape1) and col in range(self._shape2):
            if isinstance(c, Cell):
                self.spreadsheet[row][col] = deepcopy(c)
            if isinstance(c, str):
                self.spreadsheet[row][col].set_value(c)
        else:
            return "Enter valid row and column number"

    def get_cell_at(self, row, col):
        if row in range(self._shape1) and col in range(self._shape2):
            return self.spreadsheet[row][col]
        else:
            return "Enter valid row and column number"

    def add_row(self, row_num):
        if row_num in range(self._shape1):
            new_row = [Cell() for _ in range(len(self.spreadsheet[0]))]
            self.spreadsheet.insert(row_num + 1, new_row)
            self._shape1 += 1
        else:
            return "Enter valid row number"

    def remove_row(self, row_num):
        if row_num in range(self._shape1):
            del self.spreadsheet[row_num]
            self._shape1 -= 1
        else:
            return "Enter valid row number"

    def add_column(self, col_num):
        if col_num in range(self._shape2):
            for row in self.spreadsheet:
                row.insert(col_num + 1, Cell())
            self._shape2 += 1
        else:
            return "Enter valid column number"

    def remove_column(self, col_num):
        if col_num in range(self._shape2):
            for row in self.spreadsheet:
                del row[col_num]
            self._shape2 -= 1
        else:
            return "Enter valid column number"

    def swap_rows(self, row1, row2):
        if row1 in range(self._shape1) and row2 in range(self._shape1):
            self.spreadsheet[row1], self.spreadsheet[row2] = self.spreadsheet[row2], self.spreadsheet[row1]
        else:
            return "Enter valid row numbers"

    def swap_columns(self, col1, col2):
        if col1 in range(self._shape2) and col2 in range(self._shape2):
            for row in  self.spreadsheet:
                row[col1],row[col2] = row[col2], row[col1]
        else:
            return "Enter valid column numbers"



