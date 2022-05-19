from flask_admin.contrib.sqla import ModelView
from components.students_bug.models import StudentBug


class StudentBugView(ModelView):

    create_modal = True
    edit_modal = True


def load_views(admin, session):
    admin.add_view(StudentBugView(StudentBug, session))
