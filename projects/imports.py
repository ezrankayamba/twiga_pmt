import openpyxl
from . import models as p_models
from setups import models as s_models


def import_projects(excel_file):
    wb = openpyxl.load_workbook(excel_file)
    ws = wb.active
    i = 0
    for row in ws.values:
        if i:
            dict = {}
            try:
                dict['name'] = row[0]
                dict['type'] = s_models.Type.objects.get(name__icontains=row[1])
                dict['size'] = s_models.Size.objects.get(name__icontains=row[2])
                dict['start_date'] = row[3]
                dict['region'] = s_models.Region.objects.get(name__icontains=row[4])
                dict['district'] = s_models.District.objects.get(name__icontains=row[5])
                dict['town'] = row[6]
                dict['duration'] = row[7]
                dict['authority'] = s_models.Authority.objects.get(name__icontains=row[8])
                dict['quantity_demanded'] = row[9]
                dict['quantity_supplied'] = row[10]
                dict['remarks'] = row[11]
                p_models.Project.objects.create(**dict)
            except Exception as e:
                print(e)
        else:
            if len(row) < 2:
                print('Not enough columns')
                break
        i += 1
