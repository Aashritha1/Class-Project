'''from openpyxl import load_workbook
import sys,os
sys.path.append("C:\\PythonCourse\\classworkproj")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from onlineapp.models import College

wb = load_workbook('C:\\PythonCourse\\classworkproj\\onlineapp\\management\\commands\\students.xlsx')
sheet=wb.get_sheet_by_name("Colleges")
number_of_rows = sheet.max_row
number_of_columns = sheet.max_column
items = []
rows = []
for row in range(1, number_of_rows+1):
       values = []
       for col in range(1,number_of_columns+1):
           value  = (sheet.cell(row=row,column=col).value)
           values.append(value)
       item = College(*values)
       item.save()
       items.append(item)

for item in items:
    print item
    print("Accessing one single value (eg. Name): {0}".format(item.name))
'''