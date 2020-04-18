from django.db import models
from django.core.validators import RegexValidator

from accounts.models import *


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
    ('', '-'),
    ('islam', 'Islam'),
    ('buddhism', 'Buddhism'),
    ('christianity', 'Christianity'),
    ('hinduism', 'Hinduism'),
    ('chinese', 'Traditional Chinese'),
)

WOUND_FREQUENCY_CHOICES = (
    ('od', 'OD'),
    ('pd', 'PD'),
)


WOUND_LOCATION_CHOICES = (
    ('leg', 'Leg'),
    ('hand', 'Hand'),
)

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")


class Admission(PatientProfile):
    date = models.DateField()
    time = models.CharField("Time Admission", max_length=255, blank=True)
    mode = models.CharField(max_length=255, choices=MODE_CHOICES, blank=True)
#    full_name = models.CharField(max_length=255, blank=True)
#    full_name = models.ForeignKey('self', on_delete=models.CASCADE)
#    full_name = models.ForeignKey(PatientProfile, related_name='full_name_admission', to_field='full_name', on_delete=models.CASCADE)
#    ic_number = models.ForeignKey(PatientProfile, related_name='ic_number_admission', on_delete=models.CASCADE)
#    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    birth_date = models.DateField()
    age = models.IntegerField(blank=False)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, blank=True)
    marital_status = models.CharField(max_length=255, choices=MARITAL_CHOICES, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    religion = models.CharField(max_length=255, blank=True)
    occupation = models.CharField(max_length=255, blank=True)
    ec_name = models.CharField(max_length=255, blank=True)
    ec_ic_number = models.CharField('IC Number', max_length=14, blank=False)
    ec_relationship = models.CharField(max_length=255, blank=True)
    ec_phone = models.CharField(max_length=255, blank=True)
    ec_address = models.CharField(max_length=255, blank=True)
    general_condition = models.CharField(max_length=255, blank=True)
    temperature = models.CharField(max_length=255, blank=True)
    pulse = models.IntegerField(blank=False)
    BP = models.IntegerField(blank=False)
    resp = models.IntegerField(blank=False)
    spo2 = models.IntegerField(blank=False)
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
    date_discharge = models.DateField()

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


class ApplicationForHomeLeave(PatientProfile):
#    full_name = models.CharField(max_length=255, blank=True)
#    full_name = models.ForeignKey(PatientProfile, related_name='full_name_application', to_field='full_name', on_delete=models.CASCADE)
#    ic_number = models.CharField('IC Number', max_length=14, blank=False)
#    ic_number = models.ForeignKey(PatientProfile, related_name='ic_number_application', on_delete=models.CASCADE)
    patient_family_name = models.CharField(max_length=255, blank=True)
    nric_number = models.CharField('NRIC Number', validators=[ic_number_validator], max_length=14, blank=False)
    patient_family_relationship = models.CharField(max_length=255, blank=True)
    patient_family_phone = models.CharField(max_length=255, blank=True)
    patient_name = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=255, blank=True)
    signature = models.CharField(max_length=255, blank=True)
    date = models.DateField()

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Application For Home Home Leave'
        verbose_name_plural = "Application For Home Home Leave"


class Appointment(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
#    full_name = models.ForeignKey(PatientProfile, related_name='full_name_appointment', to_field='full_name', on_delete=models.CASCADE)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
#    ic_number = models.ForeignKey(PatientProfile, related_name='ic_number_appointment', on_delete=models.CASCADE)
    appointment = models.CharField(max_length=255, blank=True)
    hospital_clinic = models.CharField(max_length=255, blank=True)
    treatment_order = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = "Appointment"


class Cannulation(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    date_time = models.DateField()
    cannula_cbd_ryles_tube = models.CharField(max_length=255, blank=True)
    due_date = models.DateField()
    done_by = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Cannulation'
        verbose_name_plural = "Cannulation"


class Charges(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    date = models.DateField()
    items = models.CharField(max_length=255, blank=True)
    amount_unit = models.IntegerField(blank=False)
    given_by = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Charges'
        verbose_name_plural = "Charges"


def upload_path(instance, filename):
    return '{0}/{1}'.format('dressing_location', filename)


class Dressing(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    date = models.DateField()
    time = models.CharField(max_length=255, blank=True)
    frequency = models.CharField(max_length=255, choices=WOUND_FREQUENCY_CHOICES, blank=True)
    wound_location = models.CharField(max_length=255, choices=WOUND_LOCATION_CHOICES, blank=True)
    wound_condition = models.CharField(max_length=255, blank=True)
    photos = models.FileField(upload_to="dressing_location", blank=True)
    done_by = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Dressing'
        verbose_name_plural = "Dressing"


class EnteralFeedingRegine(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    time = models.CharField(max_length=255, blank=True)
    type_of_milk = models.CharField(max_length=255, blank=True)
    amount = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Enteral Feeding Regine'
        verbose_name_plural = "Enteral Feeding Regine"


class HGTChart(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    date = models.DateField()
    time = models.CharField(max_length=255, blank=True)
    blood_glucose_reading = models.IntegerField(blank=False)
    remark = models.CharField(max_length=255, blank=True)
    done_by = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'HGT Chart'
        verbose_name_plural = "HGT Chart"


class IntakeOutputChart(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    date = models.DateField()
    time = models.CharField(max_length=255, blank=True)
    intake_oral_type = models.CharField(max_length=255, blank=True)
    intake_oral_ml = models.CharField(max_length=255, blank=True)
    intake_parenteral_type = models.CharField(max_length=255, blank=True)
    intake_parenteral_ml = models.CharField(max_length=255, blank=True)
    intake_other_type = models.CharField(max_length=255, blank=True)
    intake_other_ml = models.CharField(max_length=255, blank=True)
    urine_ml = models.CharField(max_length=255, blank=True)
    urine_cumtotal = models.CharField(max_length=255, blank=True)
    urine_gastric_ml = models.CharField(max_length=255, blank=True)
    other_type = models.CharField(max_length=255, blank=True)
    other_ml = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Intake Output Chart'
        verbose_name_plural = "Intake Output Chart"


class Maintainance(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    date = models.DateField()
    items = models.CharField(max_length=255, blank=True)
    location_room = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    staff_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Maintainance'
        verbose_name_plural = "Maintainance"


class MedicationAdministrationRecord(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    date = models.DateField()
    items = models.CharField(max_length=255, blank=True)
    location_room = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    staff_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Medication Administration Record'
        verbose_name_plural = "Medication Administration Record"


class MedicationRecord(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    date = models.DateField()
    time = models.CharField(max_length=255, blank=True)
    medication = models.CharField(max_length=255, blank=True)
    tablet = models.IntegerField(blank=False)
    dosage = models.CharField(max_length=255, blank=True)
    frequency = models.CharField(max_length=255, blank=True)
    topup = models.CharField(max_length=255, blank=True)
    balance = models.IntegerField(blank=False)
    remark = models.CharField(max_length=255, blank=True)
    staff = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Medication'
        verbose_name_plural = "Medication"


class Nursing(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    report = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Nursing'
        verbose_name_plural = "Nursing"


class PhysioProgressNoteBack(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    report = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Physio Progress Note Back'
        verbose_name_plural = "Physio Progress Note Back"


class PhysioProgressNoteFront(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    report = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Physio Progress Note Front'
        verbose_name_plural = "Physio Progress Note Front"


class PhysiotherapyGeneralAssessment(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    doctor_diagnosis = models.CharField(max_length=255, blank=True)
    doctor_management = models.CharField(max_length=255, blank=True)
    problem = models.CharField(max_length=255, blank=True)
    pain_scale = models.CharField(max_length=255, blank=True)
    comments = models.CharField(max_length=255, blank=True)
    special_question = models.CharField(max_length=255, blank=True)
    general_health = models.CharField(max_length=255, blank=True)
    pmx_surgery = models.CharField(max_length=255, blank=True)
    observation = models.CharField(max_length=255, blank=True)
    ix_mri_x_ray = models.CharField(max_length=255, blank=True)
    medications_steroids = models.CharField(max_length=255, blank=True)
    occupation_recreation = models.CharField(max_length=255, blank=True)
    palpation = models.CharField(max_length=255, blank=True)
    pacemaker_hearing_aid = models.CharField(max_length=255, blank=True)
    splinting = models.CharField(max_length=255, blank=True)
    physical_examination_movement = models.CharField(max_length=255, blank=True)
    muscle_power = models.CharField(max_length=255, blank=True)
    functional_activities = models.CharField(max_length=255, blank=True)
    special_test = models.CharField(max_length=255, blank=True)
    date_time = models.CharField(max_length=255, blank=True)
    attending_physiotherapist = models.CharField(max_length=255, blank=True)

    current_history = models.CharField(max_length=255, blank=True)
    past_history = models.CharField(max_length=255, blank=True)
    observation = models.CharField(max_length=255, blank=True)
    palpation = models.CharField(max_length=255, blank=True)
    neurological = models.CharField(max_length=255, blank=True)
    clearing_test_other_joint = models.CharField(max_length=255, blank=True)
    physiotherapists_impression = models.CharField(max_length=255, blank=True)
    short_term_goals = models.CharField(max_length=255, blank=True)
    long_term_goals = models.CharField(max_length=255, blank=True)
    plan_treatment = models.CharField(max_length=255, blank=True)
    attending_physiotherapist = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Physiotherapy General Assessment'
        verbose_name_plural = "Physiotherapy General Assessment"


class Stool(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    date = models.DateField()
    time = models.CharField(max_length=255, blank=True)
    frequency = models.CharField(max_length=255, blank=True)
    consistency = models.CharField(max_length=255, blank=True)
    amount = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Stool'
        verbose_name_plural = "Stool"


class VitalSignFlow(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    ic_number = models.CharField('IC Number', max_length=14, blank=False)
    date = models.DateField()
    time = models.CharField(max_length=255, blank=True)
    temp = models.IntegerField(blank=False)
    pulse = models.IntegerField(blank=False)
    blood_pressure = models.IntegerField(blank=False)
    respiration = models.IntegerField(blank=False)
    spo2 = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.ic_number)

    class Meta:
        verbose_name = 'Vital Sign Flow'
        verbose_name_plural = "Vital Sign Flow"
