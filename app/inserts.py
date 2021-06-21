from models import Books
from app import db
import csv


def insert_into_table(file_name):
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        for isbn, title, author, year in reader:
            item = Books(isbn, title, author, year)
            db.session.add(item)
            db.session.commit()


if __name__ == '__main__':
    book_csv = "../books.cv"
    insert_into_table(book_csv)
