from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Index, Integer, String, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db import Base, session
import datetime
import sqlalchemy as sq
from components.users import exc
from sqlalchemy import or_

class StudentBug(Base):
    __tablename__: str = 'students_bug'

    id = sq.Column(sq.Integer, primary_key=True)
    name: str = sq.Column(sq.String)
    surname: str = sq.Column(sq.String, nullable=False)
    patronymic: str = sq.Column(sq.String)
    birthday: str = sq.Column(sq.String)
    form_study: str = sq.Column(sq.String)
    debt: int = sq.Column(sq.Integer)
    command: str = sq.Column(sq.String)
    course: str = sq.Column(sq.String)
    group: str = sq.Column(sq.String)
    faculty: str = sq.Column(sq.String)


    @classmethod
    def delete_by_id(cls, student_id):
        cls.query.filter_by(id=student_id).delete()
        session.commit()

    @classmethod
    def create_student(cls, name: str, surname: str, patronymic: str, birthday: str, form_study: str, debt: int, command: str, course: str, group: str, faculty: str):
        new_student = StudentBug()
        new_student.name = name
        new_student.surname = surname
        new_student.patronymic = patronymic
        new_student.birthday = birthday
        new_student.form_study = form_study
        new_student.debt = debt
        new_student.command = command
        new_student.course = course
        new_student.group = group
        new_student.faculty = faculty       
        session.add(new_student)
        session.commit()
        
        return new_student

    @classmethod
    def search_student(cls, data):
        data1 = session.query(cls).filter(or_(cls.name.ilike("%" + data + "%"), cls.surname.ilike("%" + data + "%"), cls.patronymic.ilike("%" + data + "%"), cls.birthday.ilike("%" + data + "%"), cls.birthday.ilike("%" + data + "%"), cls.form_study.ilike("%" + data + "%"), cls.command.ilike("%" + data + "%"), cls.faculty.ilike("%" + data + "%")))
        return data1
     
    @classmethod
    def get_all(cls):
        data = session.query(cls).all()
        return data
