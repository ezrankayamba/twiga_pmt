import io
import xlsxwriter
from . import models
from setups import models as s_models


def cell(i, j):
    char = "A"
    char = chr(ord(char[0]) + j - 1)
    return f'{char}{i}'


def setup_sheets(workbook):
    headers = ["Name", 'Contact Person', 'Position', 'Phone', 'Email', 'Location']

    def write_setup(list, s_name):
        sheet = workbook.add_worksheet(s_name)
        for j, col in enumerate(headers, start=1):
            sheet.write(f'{cell(1, j)}', col)

        for i, row in enumerate(list, start=2):
            for j, col in enumerate([row.name, row.contact_person, row.position, row.phone, row.email, row.location], start=1):
                sheet.write(f'{cell(i, j)}', col)
    write_setup(s_models.Contractor.objects.all(), 'Contractors')
    write_setup(s_models.Consultant.objects.all(), 'Consultants')
    write_setup(s_models.Supplier.objects.all(), 'Suppliers')
    write_setup(s_models.Financer.objects.all(), 'Financers')


def projects_report(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)

    main = workbook.add_worksheet("Projects")
    headers = ['Name', 'Type', 'Size', 'Start Date', 'Status', 'Region', 'District', 'Town', 'Duration(Yrs)', 'Authority', 'Qty Demanded(Tons)', 'Qty Supplied(Tons)']
    rows = []
    c_consult = 0
    c_contrac = 0
    c_supplier = 0
    c_financer = 0
    projects = models.Project.objects.all()
    for prj in projects:
        c_consult = max(c_consult, prj.consultants.count())
        c_contrac = max(c_contrac, prj.contractors.count())
        c_supplier = max(c_supplier, prj.suppliers.count())
        c_financer = max(c_financer, prj.financers.count())

    headers.extend(map(lambda x: f'Contractor {x+1}', range(c_contrac)))
    headers.extend(map(lambda x: f'Consultant {x+1}', range(c_consult)))
    headers.extend(map(lambda x: f'Supplier {x+1}', range(c_supplier)))
    headers.extend(map(lambda x: f'Financer {x+1}', range(c_financer)))

    headers.extend(['Latitude', 'Longitude', 'Remarks'])
    for prj in projects:
        row = []
        row.append(prj.name)
        row.append(prj.type.name)
        row.append(prj.size.name)
        row.append(prj.start_date.strftime("%d/%m/%Y"))
        row.append(prj.status.name)
        row.append(prj.region.name)
        row.append(prj.district.name)
        row.append(prj.town)
        row.append(prj.duration)
        row.append(prj.authority.name)
        row.append(prj.quantity_demanded)
        row.append(prj.quantity_supplied)

        # Contractors
        gap = c_contrac - prj.contractors.count()
        for e in prj.contractors.all():
            row.append(e.contractor.name)
        for _ in range(gap):
            row.append("")

        # Contractors
        gap = c_consult - prj.consultants.count()
        for e in prj.consultants.all():
            row.append(e.consultant.name)
        for _ in range(gap):
            row.append("")

        # Contractors
        gap = c_supplier - prj.suppliers.count()
        for e in prj.suppliers.all():
            row.append(e.supplier.name)
        for _ in range(gap):
            row.append("")

        # Contractors
        gap = c_financer - prj.financers.count()
        for e in prj.financers.all():
            row.append(e.financer.name)
        for _ in range(gap):
            row.append("")

        row.append(prj.latitude)
        row.append(prj.longitude)
        row.append(prj.remarks)

        rows.append(row)

    for j, col in enumerate(headers, start=1):
        main.write(f'{cell(1, j)}', col)

    for i, row in enumerate(rows, start=2):
        for j, col in enumerate(row, start=1):
            main.write(f'{cell(i, j)}', col)

    # Setup sheets
    setup_sheets(workbook)

    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data
