WOUND_FREQUENCY_CHOICES = (
    ('od', 'OD'),
    ('bd', 'BD'),
    ('tds', 'TDS'),
    ('stat', 'STAT'),
)

ADMITTED_CHOICES = (
    ('hospital', 'Hospital'),
    ('home', 'Home'),
    ('others', 'Others'),
)

MODE_CHOICES = (
    ('walkedin', 'Walked-in'),
    ('wheelchair', 'Wheelchair'),
    ('stretcher', 'Stretcher'),
)

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)

MARITAL_CHOICES = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('others', 'Others'),
)

RELIGION_CHOICES = (
    ('buddhist', 'Buddhist'),
    ('christian', 'Christian'),
    ('hinduism', 'Hinduism'),
    ('islam', 'Islam'),
    ('others', 'Others'),
)

OCCUPATION_CHOICES = (
    ('retired', 'Retired'),
    ('housewife', 'Housewife'),
    ('others', 'Others'),
)

COMMUNICATION_SIGHT_CHOICES = (
    ('good', 'Good'),
    ('poor', 'Poor'),
    ('glasses', 'Glasses'),
    ('blind', 'Blind'),
)

COMMUNICATION_HEARING_CHOICES = (
    ('good', 'Good'),
    ('poor', 'Poor'),
    ('aid', 'Aid'),
)

GENERAL_CONDITION_CHOICES = (
    ('stable', 'Stable'),
    ('ill', 'Ill'),
    ('lethargic', 'Lethargic'),
    ('weak', 'Weak'),
    ('cachexic', 'Cachexic'),
    ('coma', 'Coma'),
    ('restless', 'Restless'),
    ('depress', 'Depress'),
    ('agitated', 'Agitated'),
)

INVASIVE_LINE_INSITU_CHOICES = (
    ('-', 'None'),
    ('ett', 'ETT'),
    ('nasogastric_tube', 'Nasogastric tube'),
    ('urinary_catheter', 'Urinary catheter'),
    ('pacemaker', 'Pacemaker'),
    ('others', 'Others'),
)

MEDICAL_HISTORY_CHOICES = (
    ('nochronicillness', 'NO Chronic Illness'),
    ('asthma', 'Asthma'),
    ('diabetes_mellitus', 'Diabetes Mellitus'),
    ('hypertension', 'Hypertension'),
    ('heart_disease', 'Heart Disease'),
    ('others', 'Others'),
)

ADAPTIVE_AIDS_WITH_PATIENT_CHOICES = (
    ('denture', 'Denture'),
    ('upperset', 'Upper set'),
    ('lowerset', 'Lower set'),
    ('walkingaid', 'Walking aid'),
    ('hearingaid', 'Hearing aid'),
    ('glasses', 'Glasses'),
    ('others', 'Others'),
)

ORIENTATION_CHOICES = (
    ('nursecallsystem', 'Nurse call system'),
    ('bedmechanic', 'Bed Mechanic'),
    ('bathroom', 'Bathroom'),
    ('visiting_hours', 'Visiting hours'),
    ('careofvaluables', 'Care of Valuables'),
    ('fireexits', 'Fire Exits'),
    ('nosmokingpolicy', 'No Smoking policy'),
    ('patientrightresponsibilities', 'Patient Right/ Responsibilities'),
    ('informnurseifpatientleavingthe_center', 'Inform nurse if patient leaving the center'),
)

WOUND_LOCATION_CHOICES = (
    ('head', 'Head'),
    ('face', 'Face'),
    ('neck', 'Neck'),
    ('chest', 'Chest'),
    ('abdomen', 'Abdomen'),
    ('back', 'Back'),
    ('sacral', 'Sacral'),
    ('buttock', 'Buttock'),
    ('hand', 'Hand'),
    ('leg', 'Leg'),
    ('others', 'Others'),
)

WOUND_CONDITION_CHOICES = (
    ('clean', 'Clean'),
    ('slough', 'Slough'),
    ('eschar', 'Eschar'),
    ('Others', (
        ('Exudate', (
            ('sanguineous', 'Sanguineous'),
            ('serous', 'Serous'),
            ('haemoserous', 'Haemoserous'),
            ('purulent', 'Purulent'),
        )),
        ('Amount', (
            ('scant', 'Scant'),
            ('minimal', 'Minimal'),
            ('moderate', 'Moderate'),
            ('large', 'Large'),
        )),
    )),
)

PHYSICAL_EXAMINATION_MOVEMENT_CHOICES = (
    ('joint', 'Joint'),
    ('active', 'Active'),
    ('passive', 'Passive'),
)

STATUS_CHOICES = (
    ('-', '-'),
    ('done', 'Done'),
    ('pending', 'Pending'),
    ('cancel', 'Cancel'),
)

NEUROLOGICAL_CHOICES = (
    ('reflexes', 'Reflexes'),
    ('motor', 'Motor'),
    ('sensation', 'Sensation'),
)

STOOL_FREQUENCY_CHOICES = (
    ('-', '-'),
    ('bo', 'BO'),
    ('bno', 'BNO'),
)

CONSISTENCY_CHOICES = (
    ('-', '-'),
    ('normal', 'Normal'),
    ('hard', 'Hard'),
    ('loose', 'Loose'),
    ('watery', 'Watery'),
)

AMOUNT_CHOICES = (
    ('-', '-'),
    ('scanty', 'Scanty'),
    ('minimal', 'Minimal'),
    ('moderate', 'Moderate'),
    ('large', 'Large'),
)

BOOLEAN_CHOICES = (
    (False, 'No'),
    (True, 'Yes'),
)

YES_NO_CHOICES = (
    ('no', 'No'),
    ('yes', 'Yes'),
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

ROUTE_CHOICES = (
    ('oral', 'Oral'),
    ('iv', 'IV'),
    ('im', 'IM'),
    ('s', 'S'),
    ('c', 'C'),
    ('sl', 'SL'),
    ('rt', 'RT'),
    ('pr', 'PR'),
    ('la', 'LA'),
    ('neb', 'Neb'),
)

MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES = (
    ('od', 'OD'),
    ('om', 'OM'),
    ('pm', 'PM'),
    ('on', 'ON'),
    ('bd', 'BD'),
    ('tds', 'TDS'),
    ('qid', 'QID'),
    ('eod', 'EOD'),
    ('prn', 'PRN'),
    ('others', 'OTHERS'),
)

TAB_CHOICES = (
    ('1', '1/1 = 1 Tab'),
    ('2', '11/11 = 2 Tabs'),
    ('3', '111/111 = 3 Tabs'),
    ('half', '1/2 = Half Tab'),
    ('others', '1 1/2 = Others'),
    ('4', '4 Tabs'),
)

SIGNATURE_CHOICES = (
    ('od', 'LSS'),
    ('om', 'LPC'),
    ('pm', 'SYA'),
)
