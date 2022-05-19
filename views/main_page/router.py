from views.main_page import views


def install(app):
    app.add_url_rule(
        '/main',
        view_func=views.MainView.as_view('main-page')
    )
  
    app.add_url_rule(
        '/del_student/id=<int:student_id>',
         view_func=views.DelView.as_view('del-page')
    )

    app.add_url_rule(
        '/add_student',
        view_func=views.AddStudentView.as_view('add_student-page')
    )
    
    app.add_url_rule(
      '/update_students',
      view_func=views.StudentsUpdate.as_view('student_update-page')
    )

    app.add_url_rule(
      '/update_students/search=<string:data>',
      view_func=views.StudentsSearch.as_view('student_search-page')
    )
