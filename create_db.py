# -*- coding: utf-8 -*-
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import sqlalchemy as sq
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

import uuid



def get_vcode_now():
    v_code_now = datetime.today().strftime("%d%m%Y%H%M%S")
    return v_code_now


class DevConfig:

    DEBUG = os.environ.get('DEBUG', True)
    PORT = os.environ.get('PORT', 3040)
    HOST = os.environ.get('HOST', '0.0.0.0')

    db_name = os.environ.get('DB_NAME', 'gpk')
    db_user = os.environ.get('DB_USER', 'valy')
    db_password = os.environ.get('DB_PASSWORD', 'Elmurza0506')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', 5432)

    SECRET_KEY = os.urandom(24)
    FLASK_ADMIN_SWATCH = 'paper'


    @property
    def alchemy_url(self):
        return f'postgresql+psycopg2://{self.db_user}:{self.db_password}@' \
               f'{self.db_host}:{self.db_port}/{self.db_name}'


config = DevConfig()


engine = create_engine(config.alchemy_url)

# Session object
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Base class object for model class
Base = declarative_base()
Base.query = session.query_property()




class User(Base):
    __tablename__: str = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    login: str = sq.Column(sq.String, nullable=False, unique=True)
    password: str = sq.Column(sq.String, nullable=False)
    enum: str = sq.Column(sq.String)

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


Base.metadata.create_all(engine)



