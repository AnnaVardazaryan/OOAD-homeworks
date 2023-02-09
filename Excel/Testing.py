from Cell import Cell
from Spreadsheet import Spreadsheet


cl = Cell()

def test_result(cond, t_name):
    if cond:
        print(f"Test {t_name} is PASSED")
    else:
        print(f"Test {t_name} is FAILED")

def test_set_value():
    cl.set_value(7)
    test_result(cl.get_value() == '7', 'set_value')

def test_set_color():
    cl.set_color(4)
    test_result(cl.get_color() == '4', 'set_color')

def test_to_int():
    cl.set_value("8")
    test_result(cl.to_int() == 8, 'to_int')

def test_to_double():
    cl.set_value("11")
    test_result(cl.to_double() == 11.0, 'to_double')

def test_to_date():
    cl.set_value("09/02/23")
    test_result(str(cl.to_date()) == "2023-02-09 00:00:00", 'to_date')

def test_reset():
    cl.set_value("11")
    test_result(cl.reset() is None, 'reset')

def test_set_cell_at():
    sh = Spreadsheet(2, 2)
    cl.set_value(5)
    sh.set_cell_at(0, 0, cl)
    test_result(sh.get_cell_at(0, 0).get_value() == '5', 'set_cell_at')

def test_add_row():
    sh = Spreadsheet(2, 2)
    sh.set_cell_at(1, 0, 'el1')
    sh.add_row(0)
    test_result(sh.get_cell_at(2, 0).get_value() == 'el1' and sh._shape1 == 3, 'add_row')

def test_remove_row():
    sh = Spreadsheet(3, 2)
    sh.set_cell_at(0, 0, 'el2')
    sh.set_cell_at(2, 0, 'el3')
    sh.remove_row(1)
    test_result(sh.get_cell_at(1, 0).get_value() == 'el3' and sh._shape1 == 2, 'remove_row')

def test_add_column():
    sh = Spreadsheet(3, 3)
    sh.set_cell_at(0, 1, 'el4')
    sh.add_column(0)
    test_result(sh.get_cell_at(0, 2).get_value() == 'el4' and sh._shape2 == 4, 'add_column')

def test_remove_column():
    sh = Spreadsheet(3, 3)
    sh.set_cell_at(0, 1, 'el4')
    sh.set_cell_at(0, 2, 'el5')
    sh.remove_column(1)
    test_result(sh.get_cell_at(0, 1).get_value() == 'el5' and sh._shape2 == 2, 'remove_column')

def test_swap_rows():
    sh = Spreadsheet(3, 2)
    sh.set_cell_at(0, 0, 'el0')
    sh.set_cell_at(2, 0, 'el2')
    sh.swap_rows(0, 2)
    test_result(sh.get_cell_at(0, 0).get_value() == 'el2' and sh.get_cell_at(2, 0).get_value() == 'el0', 'swap_rows')

def test_swap_columns():
    sh = Spreadsheet(3, 2)
    sh.set_cell_at(2, 0, 'el0')
    sh.set_cell_at(2, 1, 'el1')
    sh.swap_columns(0, 1)
    test_result(sh.get_cell_at(2, 0).get_value() == 'el1' and sh.get_cell_at(2, 1).get_value() == 'el0', 'swap_columns')



def testing_cell_class():
    test_set_value()
    test_set_color()
    test_to_int()
    test_to_double()
    test_to_date()
    test_reset()

def testing_spreadsheet_class():
    test_set_cell_at()
    test_add_row()
    test_remove_row()
    test_add_column()
    test_remove_column()
    test_swap_rows()
    test_swap_columns()

testing_cell_class()
testing_spreadsheet_class()