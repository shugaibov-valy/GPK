from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Index, Integer, String, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db import Base, session
import datetime
import sqlalchemy as sq
from components.users import exc
from sqlalchemy import or_

class StudentMet(Base):
    __tablename__: str = 'students_met'

    id = sq.Column(sq.Integer, primary_key=True)
    name: str = sq.Column(sq.String)
    surname: str = sq.Column(sq.String, nullable=False)
    patronymic: str = sq.Column(sq.String)
    status: str = sq.Column(sq.String)
    education: str = sq.Column(sq.String)
    email: str = sq.Column(sq.String)
    region: str = sq.Column(sq.String)
    phone: str = sq.Column(sq.String)
    snils: str = sq.Column(sq.String)
    course: str = sq.Column(sq.String)
    group: str = sq.Column(sq.String)
    faculty: str = sq.Column(sq.String)
    birthday: str = sq.Column(sq.String)


    @classmethod
    def delete_by_id(cls, student_id):
        cls.query.filter_by(id=student_id).delete()
        session.commit()

    @classmethod
    def create_student(cls, name: str, surname: str, patronymic: str, status: str, education: str, email: str, region: str, phone: str, snils: str,  course: str, group: str, faculty: str, birthday: str):
        new_student = StudentMet()
        new_student.name = name
        new_student.surname = surname
        new_student.patronymic = patronymic
        new_student.status = status
        new_student.education = education
        new_student.email = email
        new_student.region = region
        new_student.phone = phone
        new_student.snils = snils
        new_student.course = course
        new_student.group = group
        new_student.faculty = faculty       
        new_student.birthday = birthday

        session.add(new_student)
        session.commit()
        
        return new_student

    @classmethod
    def search_student(cls, data):
        data = session.query(cls).filter(or_(cls.name.ilike("%" + data + "%"), cls.surname.ilike("%" + data + "%"), cls.patronymic.ilike("%" + data + "%"), cls.education.ilike("%" + data + "%"), cls.phone.ilike("%" + data + "%"), cls.region.ilike("%" + data + "%"), cls.snils.ilike("%" + data + "%"), cls.email.ilike("%" + data + "%"), cls.faculty.ilike("%" + data + "%"), cls.birthday.ilike("%" + data + "%")))
        return data
     
    @classmethod
    def get_all(cls):
        data = session.query(cls).all()
        return data
