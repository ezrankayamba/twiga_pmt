from django.core.management.base import BaseCommand, CommandError
import csv
from setups import models
from projects import models as prj_models


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Loading districts")
        with open('districts.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            prj_models.ProjectSupplier.objects.all().delete()
            prj_models.ProjectContractor.objects.all().delete()
            prj_models.ProjectFinancer.objects.all().delete()
            prj_models.Project.objects.all().delete()
            models.District.objects.all().delete()
            models.Region.objects.all().delete()
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    region_name = row[0].strip()
                    district_name = row[1].strip()
                    region, r_created = models.Region.objects.get_or_create(name=region_name)
                    district, d_created = models.District.objects.get_or_create(name=district_name, region=region)
