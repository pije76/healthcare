from django.utils.translation import ugettext_lazy as _

ADAPTIVE_AIDS_WITH_PATIENT_CHOICES = (
	('Denture', _('Denture')),
	('Upper set', _('Upper set')),
	('Lower set', _('Lower set')),
	('Walking aid', _('Walking aid')),
	('Glasses', _('Glasses')),
	('Others', _('Others')),
	('Hearing aid', _('Hearing aid')),
)

ADMISSION_FREQUENCY_CHOICES = (
	('OD', _('OD')),
	('OM', _('OM')),
	('PM', _('PM')),
	('ON', _('ON')),
	('BD', _('BD')),
	('TDS', _('TDS')),
	('QID', _('QID')),
	('EOD', _('EOD')),
	('PRN', _('PRN')),
	('OTHERS', _('OTHERS')),
)

ADMITTED_CHOICES = (
	('Hospital', _('Hospital')),
	('Home', _('Home')),
	('Others', _('Others')),
)


AMOUNT_CHOICES = (
	('Scanty', _('Scanty')),
	('Minimal', _('Minimal')),
	('Moderate', _('Moderate')),
	('Large', _('Large')),
	('-', _('-')),
)

BOOLEAN_CHOICES = (
	(False, _('No')),
	(True, _('Yes')),
)

COMMUNICATION_HEARING_CHOICES = (
	('Good', _('Good')),
	('Poor', _('Poor')),
	('Aid', _('Aid')),
	('Others', _('Others')),
)

COMMUNICATION_SIGHT_CHOICES = (
	('Good', _('Good')),
	('Poor', _('Poor')),
	('Glasses', _('Glasses')),
	('Blind', _('Blind')),
)

CONSISTENCY_CHOICES = (
	('Normal', _('Normal')),
	('Hard', _('Hard')),
	('Loose', _('Loose')),
	('Watery', _('Watery')),
	('-', _('-')),
)

DISCHARGE_CHECKLIST = (
	('Yes', _('Yes')),
	('No', _('No')),
	('NA', _('NA')),
)

DISCHARGE_STATUS = (
	('Ambulant', _('Ambulant')),
	('Ambulant with assistance', _('Ambulant with assistance')),
	('Death', _('Death')),
	('Wheelchair bound', _('Wheelchair bound')),
	('Bedridden', _('Bedridden')),
	('Dependant', _('Dependant')),
	('Activity of daily living', _('Activity of daily living')),
	('Independent', _('Independent')),
)

GENDER_CHOICES = (
	('Male', _('Male')),
	('Female', _('Female')),
)

GENERAL_CONDITION_CHOICES = (
	('Stable', _('Stable')),
	('Ill', _('Ill')),
	('Lethargic', _('Lethargic')),
	('Weak', _('Weak')),
	('Cachexic', _('Cachexic')),
	('Coma', _('Coma')),
	('Restless', _('Restless')),
	('Depress', _('Depress')),
	('Agitated', _('Agitated')),
)

INVASIVE_LINE_INSITU_CHOICES = (
	('ETT', _('ETT')),
	('Nasogastric Tube', _('Nasogastric Tube')),
	('Urinary Catheter', _('Urinary Catheter')),
	('Pacemaker', _('Pacemaker')),
	('Others', _('Others')),
)

MARITAL_CHOICES = (
	('Single', _('Single')),
	('Married', _('Married')),
	('Others', _('Others')),
)

MEDICAL_HISTORY_CHOICES = (
	('No Chronic Illness', _('No Chronic Illness')),
	('Asthma', _('Asthma')),
	('Diabetes Mellitus', _('Diabetes Mellitus')),
	('Hypertension', _('Hypertension')),
	('Heart Disease', _('Heart Disease')),
	('High Cholesterol', _('High Cholesterol')),
	('Dyslipidemia', _('Dyslipidemia')),
	('Others', _('Others')),
)

MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES = (
	('OD', _('OD')),
	('OM', _('OM')),
	('PM', _('PM')),
	('ON', _('ON')),
	('BD', _('BD')),
	('TDS', _('TDS')),
	('QID', _('QID')),
	('EOD', _('EOD')),
	('PRN', _('PRN')),
	('OTHERS', _('OTHERS')),
)

UNIT_CHOICES = (
	('mcg', _('mcg')),
	('mg', _('mg')),
	('gram', _('gram')),
	('unit', _('unit')),
)

MODE_CHOICES = (
	('Walked-in', _('Walked-in')),
	('Wheelchair', _('Wheelchair')),
	('Stretcher', _('Stretcher')),
)

NASOGASTRIC_TUBE_TYPE_CHOICES = (
	('PVC', _('PVC')),
	('Silicone', _('Silicone')),
)


OCCUPATION_CHOICES = (
	('Retired', _('Retired')),
	('Housewife', _('Housewife')),
	('Others', _('Others')),
)

ORIENTATION_CHOICES = (
	('Nurse call system', _('Nurse call system')),
	('Bed Mechanic', _('Bed Mechanic')),
	('Bathroom', _('Bathroom')),
	('Visiting', _('Visiting hours')),
	('Care of Valuables', _('Care of Valuables')),
	('Fire Exits', _('Fire Exits')),
	('No Smoking policy', _('No Smoking policy')),
	('Patient Right/ Responsibilities', _('Patient Right/ Responsibilities')),
	('Inform nurse if patient leaving the center', _(
		'Inform nurse if patient leaving the center')),
)

PAIN_SCALE_CHOICES = (
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', '9'),
	('10', '10'),
)

PHYSICAL_EXAMINATION_MOVEMENT_CHOICES = (
	('Joint', _('Joint')),
	('Active', _('Active')),
	('Passive', _('Passive')),
)

RELIGION_CHOICES = (
	('Buddhist', _('Buddhist')),
	('Christian', _('Christian')),
	('Hinduism', _('Hinduism')),
	('Islam', _('Islam')),
	('Others', _('Others')),
)

ROUTE_CHOICES = (
	('Oral', _('Oral')),
	('IV', 'IV'),
	('IM', 'IM'),
	('SC', 'SC'),
	('SL', 'SL'),
	('RT', 'RT'),
	('PR', 'PR'),
	('LA', 'LA'),
	('Neb', 'Neb'),
)

SIGNATURE_CHOICES = (
	('LSS', 'LSS'),
	('LPC', 'LPC'),
	('SYA', 'SYA'),
)

SOURCE_CHOICES = (
	('SK-Center', 'SK-Center'),
	('Hospital', 'Hospital'),
	('Clinic', 'Clinic'),
	('Own', 'Own'),
)

STATUS_CHOICES = (
	('Done', _('Done')),
	('Pending', _('Pending')),
	('Cancel', _('Cancel')),
)

STAT_CHOICES = (
	('NBM', 'N-NBM'),
	('Omit', 'O-Omit'),
	('Refused', 'R-Refused'),
	('Take Away', 'TA-Take Away'),
	('Taken', 'T-Taken'),
	('Withold', 'W-Withold'),
)

STOOL_FREQUENCY_CHOICES = (
	('BO', 'BO'),
	('BNO', 'BNO'),
)


SURGICAL_CHOICES = (
	('None', _('None')),
)

TAB_CHOICES = (
	('1', _('1/1 = 1 Tab')),
	('2', _('11/11 = 2 Tabs')),
	('3', _('111/111 = 3 Tabs')),
	('Half', _('1/2 = Half Tab')),
	('Others', _('1 1/2 = Others')),
	('4', _('4 Tabs')),
)

URINARY_CATHETER_TYPE_CHOICES = (
	('Latex', _('Latex')),
	('Silicone', _('Silicone')),
)

WOUND_CONDITION_CHOICES = (
	('Clean', _('Clean')),
	('Slough', _('Slough')),
	('Eschar', _('Eschar')),
	('Others', (
		('Exudate', (
			('Sanguineous', _('Sanguineous')),
			('Serous', _('Serous')),
			('Haemoserous', _('Haemoserous')),
			('Purulent', _('Purulent')),
		)),
		('Amount', (
			('Scant', _('Scant')),
			('Minimal', _('Minimal')),
			('Moderate', _('Moderate')),
			('Large', _('Large')),
		)),
	)),
)

WOUND_FREQUENCY_CHOICES = (
	('OD', 'OD'),
	('BD', 'BD'),
	('TDS', 'TDS'),
	('STAT', 'STAT'),
)

WOUND_LOCATION_CHOICES = (
	('Head', _('Head')),
	('Face', _('Face')),
	('Neck', _('Neck')),
	('Chest', _('Chest')),
	('Abdomen', _('Abdomen')),
	('Back', _('Back')),
	('Sacral', _('Sacral')),
	('Buttock', _('Buttock')),
	('Hand', _('Hand')),
	('Leg', _('Leg')),
	('Others', _('Others')),
)

YES_NO_CHOICES = (
	('No', _('No')),
	('Yes', _('Yes')),
)
