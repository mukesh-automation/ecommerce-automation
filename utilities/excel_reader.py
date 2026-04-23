import openpyxl

def get_data(file, sheet):
    wb = openpyxl.load_workbook(file)
    ws = wb[sheet]

    data = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        data.append(row)

    return data