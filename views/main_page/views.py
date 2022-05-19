from flask import redirect, render_template, url_for, request, jsonify
from components.users import exc
from components.students_bug.models import StudentBug
from flask.views import MethodView
from components.students_met.models import StudentMet
from flask import session

class MainView(MethodView):
    def get(self):
       data = []
       if session["enum"] == "бухгалтер":
           data = StudentBug.get_all()
       elif session["enum"] == "методист":
           data = StudentMet.get_all()
       return render_template("pages/main_page/index.html", data=data, enum=session["enum"])   

class DelView(MethodView):
    def get(self, student_id):
       if session["enum"] == "бухгалтер": 
           StudentBug.delete_by_id(student_id)
       elif session["enum"] == "методист":
           StudentMet.delete_by_id(student_id)
       return redirect("/main")

class AddStudentView(MethodView):
    def get(self):
        if session["enum"] == "бухгалтер":
            return render_template("pages/main_page/add_student_bug.html")
        elif session["enum"] == "методист":
            return render_template("pages/main_page/add_student_met.html")
      
    def post(self):
        if session["enum"] == "бухгалтер":
            name = request.form.get('name')
            surname = request.form.get('surname')
            patronymic: str = request.form.get('patronymic')
            birth_date: str = request.form.get('birth_date')
            form_study: str = request.form.get('form_study')
            debt: int = request.form.get('debt')
            command: str = request.form.get('command')
            course: str = request.form.get('course')
            group: str = request.form.get('group')
            faculty: str = request.form.get('faculty')
        
            StudentBug.create_student(name, surname, patronymic, birth_date, form_study, debt, command, course, group, faculty)
            return redirect("/main")
            
        elif session["enum"] == "методист":
            name = request.form.get('name')
            surname = request.form.get('surname')
            patronymic: str = request.form.get('patronymic')
            status: str = request.form.get('status')
            education: str = request.form.get('education') 
            email: str = request.form.get('email') 
            region: str = request.form.get('region')  
            phone: str = request.form.get('phone')
            snils: str = request.form.get('snils')
            course: str = request.form.get('course')
            group: str = request.form.get('group')
            faculty: str = request.form.get('faculty')
            birth_date: str = request.form.get('birth_date') 
            StudentMet.create_student(name, surname, patronymic, status, education, email, region, phone, snils, course, group, faculty, birth_date)
            return redirect('/main')           



class StudentsSearch(MethodView):    ## /update_students/search=<string:data>
    def get(self):
        pass

    def post(self, data):            
        if session["enum"] == "бухгалтер":
            data = StudentBug.search_student(data)
        elif session["enum"] == "методист":
            data = StudentMet.search_student(data)
        return jsonify('', render_template('pages/main_page/table_students_model.html', data=data, enum=session["enum"]))

class StudentsUpdate(MethodView):    ## /update_students
    def get(self):
        pass

    def post(self):
        data = []
        if session["enum"] == "бухгалтер":
            data = StudentBug.get_all()
        elif session["enum"] == "методист":
            data = StudentMet.get_all()
        return jsonify('', render_template('pages/main_page/table_students_model.html', data=data, enum=session["enum"]))

