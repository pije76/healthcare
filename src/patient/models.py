from django.db import models

MODE_CHOICES = (
    ('ambulance', 'Ambulance'),
    ('own', 'Own Transport'),
)

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    ic_number = models.IntegerField()

    def __str__(self):
        return str(self.full_name)


class Admission(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    time = models.CharField(max_length=100)
    mode = models.CharField(max_length=100, choices=MODE_CHOICES)
    full_name = models.ForeignKey(Patient, related_name='fullname', on_delete=models.CASCADE)
    ic_number = models.ForeignKey(Patient, related_name='icnumber', on_delete=models.CASCADE)
    birth_date = models.DateTimeField(auto_now=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    ec_name = models.CharField(max_length=100)
    ec_ic_number = models.IntegerField()
    ec_relationship = models.CharField(max_length=100)
    ec_phone = models.CharField(max_length=100)
    ec_address = models.CharField(max_length=100)
    general_condition = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    pulse = models.IntegerField()
    BP = models.CharField(max_length=100)
    resp = models.IntegerField()
    spo2 = models.IntegerField()
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
    date_discharge = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.full_name)


class ApplicationForHomeCareHomeLeave(models.Model):
    full_name = models.ForeignKey(Patient, related_name='name_homeleave', on_delete=models.CASCADE)
    ic_number = models.ForeignKey(Patient, related_name='icnumber_homeleave', on_delete=models.CASCADE)
    date_time_of_appointment = models.CharField(max_length=100)
    hospital_clinic = models.CharField(max_length=100)
    treatment_order = models.CharField(max_length=100)

    def __str__(self):
        return str(self.full_name)


class Appointment(models.Model):
    full_name = models.ForeignKey(Patient, related_name='name_appointment', on_delete=models.CASCADE)
    ic_number = models.ForeignKey(Patient, related_name='icnumber_appointment', on_delete=models.CASCADE)
    date_time = models.CharField(max_length=100)
    hospital_clinic = models.CharField(max_length=100)
    treatment_order = models.CharField(max_length=100)

    def __str__(self):
        return str(self.full_name)


class Cannulation(models.Model):
    full_name = models.ForeignKey(Patient, related_name='name_cannulation', on_delete=models.CASCADE)
    ic_number = models.ForeignKey(Patient, related_name='icnumber_cannulation', on_delete=models.CASCADE)
    date_time = models.CharField(max_length=100)
    cannula_cbd_ryles_tube = models.CharField(max_length=100)
    due_date = models.CharField(max_length=100)
    done_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.full_name)


class ChargesSheet(models.Model):
    full_name = models.ForeignKey(Patient, related_name='name_chargessheet', on_delete=models.CASCADE)
    ic_number = models.ForeignKey(Patient, related_name='icnumber_chargessheet', on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    items = models.CharField(max_length=100)
    amount_unit = models.CharField(max_length=100)
    given_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.full_name)


def upload_path(instance, filename):
    return '{0}/{1}'.format('photo', filename)


class DressingChart(models.Model):
    full_name = models.ForeignKey(Patient, related_name='name_dressing', on_delete=models.CASCADE)
    ic_number = models.ForeignKey(Patient, related_name='icnumber_dressing', on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    type_frequency_of_dressing = models.CharField(max_length=100)
    wound_condition = models.CharField(max_length=100)
    photo = models.FileField(upload_to="upload_path", null=True, blank=True)
    done_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.full_name)


class EnteralFeedingRegine(models.Model):
    full_name = models.ForeignKey(Patient, related_name='name_feeding', on_delete=models.CASCADE)
    ic_number = models.ForeignKey(Patient, related_name='icnumber_feeding', on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    type_frequency_of_dressing = models.CharField(max_length=100)
    wound_condition = models.CharField(max_length=100)
    done_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.full_name)


class HGTChart(models.Model):
    full_name = models.ForeignKey(Patient, related_name='name_hgt', on_delete=models.CASCADE)
    ic_number = models.ForeignKey(Patient, related_name='icnumber_hgt', on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    blood_glucose_reading = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    done_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.full_name)


class IntakeOutputChart(models.Model):
    full_name = models.ForeignKey(Patient, related_name='name_intake', on_delete=models.CASCADE)
    ic_number = models.ForeignKey(Patient, related_name='icnumber_intake', on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    type_frequency_of_dressing = models.CharField(max_length=100)
    wound_condition = models.CharField(max_length=100)
    done_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.full_name)
