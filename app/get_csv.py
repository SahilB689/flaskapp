# -*- coding=utf-8 -*-

from base import Base, Session, engine, Books
from sqlalchemy.exc import IntegrityError
import csv

# generate database schema
Base.metadata.create_all(engine)

# create a new session
session = Session()


def insert_into_table(file_name):
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        for isbn, title, author, year in reader:
            try:
                item = Books(isbn, title, author, year)
                session.add(item)
                session.commit()
            except IntegrityError:
                session.rollback()
                pass
        session.close()


if __name__ == '__main__':
    book_csv = "../books.csv"
    insert_into_table(book_csv)
