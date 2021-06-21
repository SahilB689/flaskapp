# -*- coding=utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine("postgresql://postgres:8@ttle#1eld5@localhost:5432/cs50")
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    isbn = Column(String(10))
    title = Column(String(100))
    author = Column(String)
    year = Column(Integer)

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"
