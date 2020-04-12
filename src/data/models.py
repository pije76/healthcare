from django.db import models

from patient.models import *


MODE_CHOICES = (
    ('ambulance', 'Ambulance'),
    ('own', 'Own Transport'),
)

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)

MARITAL_CHOICES = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
)

RELIGION_CHOICES = (
    ('islam', 'Islam'),
    ('buddhism', 'Buddhism'),
    ('christianity', 'Christianity'),
    ('hinduism', 'Hinduism'),
    ('chinese', 'Traditional Chinese'),
)

WOUND_CHOICES = (
    ('od', 'OD'),
    ('pd', 'PD'),
)


class Admission(models.Model):
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    time = models.CharField("Time Admission", max_length=255, blank=True)
    mode = models.CharField(max_length=255, choices=MODE_CHOICES, blank=True)
#    full_name = models.ForeignKey(UserProfile, related_name='full_name_admission', to_field='full_name', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, unique=True)
#    ic_number = models.AutoField('IC Number', primary_key=True, editable=False)
    ic_number = models.CharField('IC Number', max_length=14, validators=[RegexValidator(r'^\d\d\d\d-\d\d-\d\d$')], unique=True)
#    ic_number = models.ForeignKey(UserProfile, related_name='ic_number_admission', to_field='ic_number', on_delete=models.CASCADE)
#    ic_number = models.IntegerField('IC Number', max_length=255, unique=True, default=number)
#    ic_number = models.IntegerField(default=count_numbers)
    birth_date = models.DateTimeField("Birth Date", auto_now=True, blank=True)
    age = models.IntegerField(null=True, blank=False)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, blank=True)
    marital_status = models.CharField(max_length=255, choices=MARITAL_CHOICES, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    religion = models.CharField(max_length=255, blank=True)
    occupation = models.CharField(max_length=255, blank=True)
    ec_name = models.CharField(max_length=255, blank=True)
    ec_ic_number = models.IntegerField(null=True, blank=False)
    ec_relationship = models.CharField(max_length=255, blank=True)
    ec_phone = models.CharField(max_length=255, blank=True)
    ec_address = models.CharField(max_length=255, blank=True)
    general_condition = models.CharField(max_length=255, blank=True)
    temperature = models.CharField(max_length=255, blank=True)
    pulse = models.IntegerField(null=True, blank=False)
    BP = models.IntegerField(null=True, blank=False)
    resp = models.IntegerField(null=True, blank=False)
    spo2 = models.IntegerField(null=True, blank=False)
    medication = models.CharField(max_length=255, blank=True)
    food = models.CharField(max_length=255, blank=True)
    others = models.CharField(max_length=255, blank=True)
    biohazard_infectious_disease = models.CharField(max_length=255, blank=True)
    medical_history = models.CharField(max_length=255, blank=True)
    surgical_history = models.CharField(max_length=255, blank=True)
    diagnosis = models.CharField(max_length=255, blank=True)
    own_medication = models.CharField(max_length=255, blank=True)
    denture = models.CharField(max_length=255, blank=True)
    admission_by = models.CharField(max_length=255, blank=True)
    date_discharge = models.DateTimeField("Date Discharge", auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.ic_number)

    def number():
        no = Admission.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    def count_numbers():
        max_value = Admission.objects.all().aggregate(Max('ic_number'))
#        query = list(Admission.objects.order_by('-ic_number')[:1])
        return max_value['ic_number__max'] + 1
#        return query[0] + 1 if query else 0

    class Meta:
        verbose_name = 'Admission'
        verbose_name_plural = "Admission"


class ApplicationForHomeLeave(models.Model):
    ic_number = models.ForeignKey(UserProfile, related_name='ic_number2', on_delete=models.CASCADE)
    full_name = models.ForeignKey(UserProfile, related_name='full_name2', on_delete=models.CASCADE)
    date_time_of_appointment = models.DateTimeField("Date Appointment", auto_now_add=True, blank=True)
    hospital_clinic = models.CharField(max_length=255)
    treatment_order = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Application For Home Home Leave'
        verbose_name_plural = "Application For Home Home Leave"


class Appointment(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    appointment = models.CharField(max_length=255)
    hospital_clinic = models.CharField(max_length=255)
    treatment_order = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = "Appointment"


class Cannulation(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date_time = models.CharField(max_length=255)
    cannula_cbd_ryles_tube = models.CharField(max_length=255)
    due_date = models.DateTimeField("Due Date", auto_now_add=True, blank=True)
    done_by = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Cannulation'
        verbose_name_plural = "Cannulation"


class Charges(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    items = models.CharField(max_length=255)
    amount_unit = models.IntegerField(null=True, blank=False)
    given_by = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Charges'
        verbose_name_plural = "Charges"


def upload_path(instance, filename):
    return '{0}/{1}'.format('wound_location', filename)


class Dressing(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    time = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255, choices=WOUND_CHOICES, blank=True)
    wound_condition = models.CharField(max_length=255)
    wound_location = models.FileField(upload_to="upload_path", null=True, blank=True)
    done_by = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Dressing'
        verbose_name_plural = "Dressing"


class EnteralFeedingRegine(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    time = models.CharField(max_length=255)
    type_of_milk = models.CharField(max_length=255)
    amount = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Enteral Feeding Regine'
        verbose_name_plural = "Enteral Feeding Regine"


class HGTChart(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    time = models.CharField(max_length=255)
    blood_glucose_reading = models.IntegerField(null=True, blank=False)
    remark = models.CharField(max_length=255)
    done_by = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'HGT Chart'
        verbose_name_plural = "HGT Chart"


class IntakeOutputChart(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    time = models.CharField(max_length=255)
    type_frequency_of_dressing = models.CharField(max_length=255)
    wound_condition = models.CharField(max_length=255)
    done_by = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Intake Output Chart'
        verbose_name_plural = "Intake Output Chart"


class Maintainance(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    items = models.CharField(max_length=255)
    location_room = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    staff_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Maintainance'
        verbose_name_plural = "Maintainance"


class MedicationAdministrationRecord(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    items = models.CharField(max_length=255)
    location_room = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    staff_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Medication Administration Record'
        verbose_name_plural = "Medication Administration Record"


class MedicationRecord(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    time = models.CharField(max_length=255)
    medication = models.CharField(max_length=255)
    tablet = models.IntegerField(null=True, blank=False)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    topup = models.CharField(max_length=255)
    balance = models.IntegerField(null=True, blank=False)
    remark = models.CharField(max_length=255)
    staff = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Medication'
        verbose_name_plural = "Medication"


class Nursing(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    items = models.CharField(max_length=255)
    location_room = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    staff_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Nursing'
        verbose_name_plural = "Nursing"


class PhysioProgressNoteBack(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    items = models.CharField(max_length=255)
    location_room = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    staff_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Physio Progress Note Back'
        verbose_name_plural = "Physio Progress Note Back"


class PhysioProgressNoteFront(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    items = models.CharField(max_length=255)
    location_room = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    staff_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Physio Progress Note Front'
        verbose_name_plural = "Physio Progress Note Front"


class PhysiotherapyGeneralAssessment(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    doctor_diagnosis = models.CharField(max_length=255)
    doctor_diagnosis = models.CharField(max_length=255)
    problem = models.CharField(max_length=255)
    pain_scale = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    current_history = models.CharField(max_length=255)
    special_question = models.CharField(max_length=255)
    past_history = models.CharField(max_length=255)
    general_health = models.CharField(max_length=255)
    pmx_surgery = models.CharField(max_length=255)
    observation = models.CharField(max_length=255)
    ix_mri_x_ray = models.CharField(max_length=255)
    medications_steroids = models.CharField(max_length=255)
    occupation_recreation = models.CharField(max_length=255)
    palpation = models.CharField(max_length=255)
    pacemaker_hearing_aid = models.CharField(max_length=255)
    splinting = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Physiotherapy General Assessment'
        verbose_name_plural = "Physiotherapy General Assessment"


class Stool(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    time = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    consistency = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Stool'
        verbose_name_plural = "Stool"


class VitalSignFlow(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    ic_number = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField("Date", auto_now_add=True, blank=True)
    time = models.CharField(max_length=255)
    temp = models.IntegerField(null=True, blank=False)
    pulse = models.IntegerField(null=True, blank=False)
    blood_pressure = models.IntegerField(null=True, blank=False)
    respiration = models.IntegerField(null=True, blank=False)
    spo2 = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Vital Sign Flow'
        verbose_name_plural = "Vital Sign Flow"
