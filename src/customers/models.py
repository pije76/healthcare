from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Domain(DomainMixin):
    pass


MODE = (
    ('Ambulance', 'Ambulance'),
    ('Own', 'Own Transport'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class Admission(models.Model):
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    mode = models.CharField(max_length=100, choices=MODE, default='Ambulance')
    full_name = models.CharField(max_length=100)
    ic_number = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER, default='Male')
    marital_status = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    ec_name = models.CharField(max_length=100)
    ec_ic_number = models.CharField(max_length=100)
    ec_relationship = models.CharField(max_length=100)
    ec_phone = models.CharField(max_length=100)
    ec_address = models.CharField(max_length=100)
    general_condition = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    pulse = models.CharField(max_length=100)
    BP = models.CharField(max_length=100)
    resp = models.CharField(max_length=100)
    spo2 = models.CharField(max_length=100)
    medication = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    others = models.CharField(max_length=100)
    biohazard_infectious_disease = models.CharField(max_length=100)
    medical_history = models.CharField(max_length=100)
    surgical_history = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    own_medication = models.CharField(max_length=100)
    denture = models.CharField(max_length=100)
    admission_by = models.CharField(max_length=100)
    date_discharge = models.CharField(max_length=100)
