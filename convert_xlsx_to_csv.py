import pandas as pd
import csv

def convert_xlsx_to_csv(xlsx_file, csv_file):
    # Read the Excel file
    df = pd.read_excel(xlsx_file)
    
    # Write to CSV file with quoting
    df.to_csv(csv_file, index=False, quoting=csv.QUOTE_NONNUMERIC)

xlsx_file_path = 'file/path.xlsx'
csv_file_path = 'file/path.csv'

convert_xlsx_to_csv(xlsx_file_path, csv_file_path)
