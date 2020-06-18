from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import schedule1

visit_schedule1 = VisitSchedule(
    name='visit_schedule1',
    verbose_name='Trainee',
    offstudy_model='trainee_prn.subjectoffstudy',
    locator_model='trainee_subject.subject_locator',
    death_report_model='trainee_subject.death_report',
    previous_visit_schedule=None)

visit_schedule1.add_schedule(schedule1)

site_visit_schedules.register(visit_schedule1)
