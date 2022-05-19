from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Index, Integer, String, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db import Base, session
import sqlalchemy as sq
from components.users import exc


class User(Base):
    __tablename__: str = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    login: str = sq.Column(sq.String, nullable=False, unique=True)
    password: str = sq.Column(sq.String, nullable=False)
    enum: str = sq.Column(sq.String)

    @classmethod
    def create_user(cls, login: str, password: str, enum: str):
        new_user = User()
        new_user.login = login
        new_user.password = password
        new_user.enum = enum
       
        session.add(new_user)
        session.commit()
        
        return new_user

    @classmethod
    def login_check(cls, login, password):
        user = session.query(cls).filter(
                cls.login == login, 
                cls.password == password).first()
        if not user:
            raise exc.AuthLoginUserNotFound
        return user
