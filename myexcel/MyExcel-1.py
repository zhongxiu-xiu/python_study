# -*-coding:UTF-8 -*-
from myexcel.demo import cell_value


class MyExcel():
    def __init__(self,workbook_name,sheet_name):
        self.workbook_name=workbook_name
        self,sheet_name=sheet_name
        
        def __init__(self):
            bk=open_workbook(self.workbook_name)
            sheet=bk.sheet_by_name(self.sheet_name)
            return sheet
        
    #  读总行数
    def total_rows(self):
        return self._sheet().nrows
    
    # 读总列数
    def total_row(self):
         return self._sheet().ncols
      
    # 读单元格值
    def cell_value(self,row,col): 
         cell_value =self._sheet().cell_value(row,col)
         return cell_value
     
    # 读某行值
     

