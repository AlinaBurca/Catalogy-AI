import openpyxl
import re

path_database = r'C:\Users\burca\OneDrive\Desktop\UNI\ANUL_III\SEM_1\AI\Tema1\Data cat personality and predation Cordonnier et al.xlsx'
workbook = openpyxl.load_workbook(path_database)
sheet = workbook['Data']

print("Setul de date este urmatorul:")
for row in sheet.iter_rows(values_only=True):
    print(row)