# -*-coding:UTF-8 -*-
from xlrd import open_workbook

bk=open_workbook(r'd:\emp.xls')
sheet=bk.sheet_by_name('empinfo')
print(sheet.norows)
# 读有多少列
print(sheet.nrows)

# 读某单元格（ANALYST)
row_values=sheet.row_value(6,4)
print(row_values)


# 读整个第X（7）行数据
class MyExcel():
    def_init_(self,cell_name,value_name):
    
    
# 读姓名这一列

# 读整个列表数据
