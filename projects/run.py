from projects import models as p_models
from setups import models as s_models


def make_all_caps(types):
    for t in types:
        for item in t.objects.all():
            fields = ["name", "town", "supplier", "group", "client"]
            for f in fields:
                if hasattr(item, f):
                    value = getattr(item, f)
                    value = value.upper() if value else value
                    setattr(item, f, value)
                    # print(f, value)
            try:
                item.save()
            except:
                print("Error: ", item)


def execute():
    types = [p_models.Project, p_models.ProjectSupplier, s_models.Type,
             s_models.Brand, s_models.Consultant, s_models.Contractor, s_models.Financer,
             s_models.Supplier, s_models.Type, s_models.Size, s_models.Status, s_models.Region, s_models.District]
    make_all_caps(types)
