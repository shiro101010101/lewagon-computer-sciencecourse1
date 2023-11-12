# pylint: disable=missing-docstring, C0103
import sqlite3


def directors_count(db):
    # return the number of directors contained in the database
    query ="""SELECT * FROM directors;
    """
    db.execute(query)
    rows = db.fetchall()
    return len(rows)

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query ="""SELECT * FROM directors
    ORDER BY name ASC
    """
    db.execute(query)
    rows = db.fetchall()

    lis=[]
    for rows in rows:
        lis.append(rows[0])
    return lis


def love_movies(db):
    # return the list of all movies which
    # contain the word "love" in their title, sorted in alphabetical order
    # return the list of all the directors sorted in alphabetical order
    query = """SELECT * FROM movies
    WHERE title LIKE '%love%'
    ORDER BY title ASC;
    """
    db.execute(query)
    rows = db.fetchall()

    lis=[]
    for rows in rows:
        lis.append(rows[0])
    return lis
    # list(map(lambda x: x[0], results))


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = f"""SELECT COUNT(*) FROM directors
    WHERE name LIKE '%{name}%'
    ORDER BY name ASC;
    """
    db.execute(query)
    num = db.fetchall()
    return num[0][0]


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration, sorted in the alphabetical order
    query = f"""SELECT * FROM movies
    WHERE minutes > {min_length}
    ORDER BY title ASC;
    """
    db.execute(query)
    rows = db.fetchall()

    lis=[]
    for rows in rows:
        lis.append(rows[0])
    return lis
