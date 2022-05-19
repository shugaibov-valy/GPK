from flask_admin.contrib.sqla import ModelView
from components.students_met.models import StudentMet


class StudentMetView(ModelView):

    create_modal = True
    edit_modal = True


def load_views(admin, session):
    admin.add_view(StudentMetView(StudentMet, session))
