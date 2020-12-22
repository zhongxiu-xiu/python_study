# -*-coding:UTF-8 -*-
from xlrd import open_workbook
 
bk=open_workbook(r'd:\emp.xls')
sheet=bk.sheet_by_name('empinfo')
print(sheet.nrows)

print(sheet.ncols)

row_values=sheet.row_value(6,4)
print(row_values)


class MyExcel():
    def __init__(self,cell_name,value_name):
    
cell_value=sheet.cell_value(12,6)
print(cell_value)

