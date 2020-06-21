from edc_visit_schedule import FormsCollection, Crf

crf = {}
crfs_1000 = FormsCollection(
    Crf(show_order=2, model='trainee_subject.educationquestionnaire'),
    Crf(show_order=3, model='trainee_subject.communityquestionnaire'),
    name='enrollment')
crf.update({1000: crfs_1000})

crfs_1300 = FormsCollection(
    Crf(show_order=1, model='trainee_subject.educationquestionnaire'),
    Crf(show_order=2, model='trainee_subject.communityquestionnaire'),
    name='month3')
crf.update({1300: crfs_1300})

crfs_1600 = FormsCollection(
    Crf(show_order=1, model='trainee_subject.educationquestionnaire'),
    Crf(show_order=2, model='trainee_subject.communityquestionnaire'),
    name='month6')
crf.update({1600: crfs_1600})

crfs_1900 = FormsCollection(
    Crf(show_order=1, model='trainee_subject.educationquestionnaire'),
    Crf(show_order=2, model='trainee_subject.communityquestionnaire'),
    name='month12')
crf.update({1900: crfs_1900})

crfs_2200 = FormsCollection(
    Crf(show_order=1, model='trainee_subject.educationquestionnaire'),
    Crf(show_order=2, model='trainee_subject.communityquestionnaire'),
    name='month15')
crf.update({2200: crfs_2200})

_crfs = FormsCollection(
    Crf(show_order=1, model='trainee_subject.educationquestionnaire'),
    Crf(show_order=2, model='trainee_subject.communityquestionnaire'))

start_point = 2200
for _ in range(16):
    start_point += 300
    crf.update({start_point: _crfs})
